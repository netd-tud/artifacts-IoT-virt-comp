#!/usr/bin/env python3

import re
import yaml
import csv
import math
import argparse
from collections import defaultdict


class ConfigSource:
    def gen_values_to_update(self, src: str):
        pass

    def gen_default_dict(self, depth: int, last_type: type):
        if depth == 1:
            return defaultdict(last_type)
        return defaultdict(lambda: self.gen_default_dict(depth - 1, last_type))


class CsvConfigSource(ConfigSource):
    def gen_values_to_update(self, src: str):
        result = self.gen_default_dict(depth=4, last_type=int)
        with open(src, newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            vari_set = set(reader.fieldnames) - {"iterations", "scale_factor", "board" ,"benchmark", "environment"}
            for r in reader:
                for v in vari_set:
                    if not r.get(v):
                        continue
                    result[r["board"]][r["benchmark"]][r["environment"]][v] = int(r[v])
        return result, vari_set


class LogConfigSource(ConfigSource):
    PATTERN = r"=== ([a-zA-Z0-9-_]+) for ([a-zA-Z0-9-_]+) (\w+)=(\d+) ==="

    def gen_values_to_update(self, src: str):
        result = self.gen_default_dict(depth=4, last_type=int)
        vari_set = set()
        with open(src, "r") as file:
            for line in file:
                match = re.match(self.PATTERN, line.strip())
                if match:
                    bench, lang, vari, value = match.groups()
                    result["nrf52840dk"][bench][lang][vari] = int(value)
                    vari_set.add(vari)
        return result, vari_set


def main():
    args = argparse.ArgumentParser()
    args.add_argument("command", choices=["log", "csv"])
    args.add_argument("--source", required=True)
    args.add_argument("--output", required=True)
    args.add_argument("--margin", required=False, default=1.1, type=float)
    args = args.parse_args()

    if args.command == "log":
        parser = LogConfigSource()
    elif args.command == "csv":
        parser = CsvConfigSource()

    values_to_update, vari_set = parser.gen_values_to_update(args.source)
    assert values_to_update.keys() != ["nrf52840dk"], "This only supports the nrf52840dk as of now."
    values_to_update = values_to_update["nrf52840dk"]

    try:
        with open(args.output, "r") as yaml_file:
            yaml_data = yaml.safe_load(yaml_file) or {}
    except FileNotFoundError as e:
        print(f"YAML input file '{args.output}' not found.")
        raise e

    for b in yaml_data["benchmarks"]:
        assert b["boards"][0]["board_name"] == "nrf52840dk", "This only supports the nrf52840dk as of now."
        for se in b["boards"][0]["supported_environments"]:
            for v in vari_set:
                old = se["env"].get(v.upper(), None)
                if old is None:
                    continue
                new = values_to_update[b.get("name")][se.get("label", se.get("name"))].get(v)
                if new is None:
                    print(f"{b.get("name")} on {se.get("label", se.get("name"))} {v} had no value!")
                    continue
                # We add a margen (default 10%) to all values
                new = math.ceil(new * args.margin)
                print(f"{b.get("name")} on {se.get("label", se.get("name"))} {v}={old} -> {new}")
                se["env"][v.upper()] = new

    with open(args.output, "w") as yaml_file:
        yaml.safe_dump(yaml_data, yaml_file, sort_keys=False)

    print(f"Data has been written to {args.output}")


if __name__ == "__main__":
    main()
