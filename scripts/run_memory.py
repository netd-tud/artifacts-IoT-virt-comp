#!/usr/bin/env python3

import os
import json
import yaml
import csv
import argparse
import subprocess
import sys
from enum import Enum

from elftools.elf.elffile import ELFFile

from config import Config


class SymbolType(Enum):
    """Symbol section types as reported by cosy.

    Known codes:
    - 't' -> .text
    - 'd' -> .data
    - 'b' -> .bss
    - 'r' -> .rodata
    Any unknown code maps to UNKNOWN.
    """

    TEXT = "t"
    DATA = "d"
    BSS = "b"
    RODATA = "r"
    UNKNOWN = "?"

    @classmethod
    def from_code(cls, code: str) -> "SymbolType":
        if not code:
            return cls.UNKNOWN
        c = code.lower()
        if c == "t":
            return cls.TEXT
        if c == "d":
            return cls.DATA
        if c == "b":
            return cls.BSS
        if c == "r":
            return cls.RODATA
        return cls.UNKNOWN

    @property
    def section(self) -> str:
        return {
            SymbolType.TEXT: ".text",
            SymbolType.DATA: ".data",
            SymbolType.BSS: ".bss",
            SymbolType.RODATA: ".rodata",
            SymbolType.UNKNOWN: "unknown"
        }.get(self)


def load_mappings(mappings_file):
    """Load mappings keyed by board name with a 'default' fallback.

        Expected YAML structure:
            mappings:
                default:
                    - category: Runtime
                      prefixes:
                        - [app, benchmark]
                        - [pkg, lua]
                adafruit-feather-nrf52840-sense:
                    - category: App
                      prefixes:
                        - [pkg, lua]

    Returns a dict: { board_name: { (prefix_tuple) : category, ... }, 'default': {...} }
    """
    if not mappings_file:
        return {}
    try:
        with open(mappings_file) as f:
            data = yaml.safe_load(f) or {}

        mappings_node = data.get('mappings')
        if not isinstance(mappings_node, dict):
            raise RuntimeError(
                "'mappings' must be a mapping keyed by board names (use 'default' for fallback)")

        board_mappings: dict[str, dict[tuple, str]] = {}
        for env_name, entries in mappings_node.items():
            if entries is None:
                board_mappings[str(env_name)] = {}
                continue

            if not isinstance(entries, list):
                raise RuntimeError(
                    f"mappings['{env_name}'] must be a list of category entries"
                )

            for entry in entries:
                if not isinstance(entry, dict):
                    continue

                category = entry.get("category")
                prefixes = entry.get("prefixes", [])

                if not category or not prefixes:
                    continue

                if not isinstance(prefixes, list):
                    continue

                for prefix_list in prefixes:
                    if not isinstance(prefix_list, list):
                        continue

                    prefix_tuple = tuple(prefix_list)
                    board_mappings.setdefault(str(env_name), {})[prefix_tuple] = (
                        category
                    )

        return board_mappings
    except Exception as e:
        raise RuntimeError(f"Error loading mappings file: {e}")


def process_symbols(symbols: list[dict], mappings: dict, board_name: str):
    """Aggregate sizes per (category, type) with board-specific mappings.

    - mappings: dict returned by load_mappings() keyed by board names and 'default'.
    - board_name: current board name used to select mappings.
    Returns a dict keyed by (category, SymbolType) -> total size.
    """
    board_map = mappings.get(board_name, {})
    default_map = mappings.get("default", {})

    mappings = default_map | board_map

    agg = {}
    for sym in symbols:
        path = sym.get('path', [])
        if not path:
            continue

        sym_name = sym.get('sym')
        if sym_name is not None and sym_name != "":
            path.append(sym_name)

        size = sym.get('size', 0)
        if not size:
            continue
        stype = SymbolType.from_code(sym.get('type'))

        # Check mappings: prefer board-specific, then default
        matched = False
        for prefix, cat in mappings.items():
            prefix = list(prefix)
            if len(prefix) > len(path):
                continue
            prefix_end = prefix[-1] if prefix else ""
            prefix_rest = prefix[:-1]
            path_cursor = path[len(prefix) - 1]
            prefix_end_matched = False

            if prefix_end.startswith("*") and prefix_end.endswith("*"):
                prefix_end_matched = prefix_end[1:-1] in path_cursor
            elif prefix_end.endswith("*"):
                prefix_end_matched = path_cursor.startswith(prefix_end[:-1])
            elif prefix_end.startswith("*"):
                prefix_end_matched = path_cursor.endswith(prefix_end[1:])
            else:
                prefix_end_matched = prefix_end == path_cursor

            if prefix_end_matched and prefix_rest == path[: len(prefix) - 1]:
                matched = True
                cat_name = cat
                break

        if not matched and size > 5:
            print(f"path: {'/'.join(path)} not matched [size = {size}, type = {stype}]")
            cat_name = f"Unknown Symbols{f' ({path[0]})' if path else ''}"

        key = (cat_name, stype)
        agg[key] = agg.get(key, 0) + size
    return agg


def run_make_cosy(env_dir, board_name, filename, env_vars):
    """Run 'make all' then 'make cosy-output' and return the symbols filename."""
    env = os.environ.copy()
    added_env = {}
    added_env["BOARD"] = board_name
    added_env["BENCHMARK"] = filename
    added_env.update({k: str(v) for k, v in env_vars.items()})

    print(f"  Configuration: {added_env}")

    env |= added_env

    # 1) Build everything first
    print(f"  Running 'make all'...", end="")
    sys.stdout.flush()
    build_proc = subprocess.run(
        ['make', 'all'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=env_dir,
        env=env,
    )
    if build_proc.returncode != 0:
        print(" failed!")
        raise subprocess.CalledProcessError(build_proc.returncode, 'make all')
    print(" done")

    # 2) Generate cosy output
    print(f"  Running 'make cosy-output'...", end="")
    sys.stdout.flush()
    process = subprocess.run(
        ['make', 'cosy-output'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=env_dir,
        env=env,
    )
    if process.returncode != 0:
        print(" failed!")
        raise subprocess.CalledProcessError(process.returncode, 'make cosy-output')
    print(" done")

    return 'symbols.json'


def analyze_elf_sizes(elf_path):
    """Analyze an ELF file and return total size and individual section sizes.

    - Total size: Sum of all section sizes.
    - Individual sections: Dict of section names to sizes.

    Args:
        elf_path (str): Path to the ELF file.

    Returns:
        dict: {'total_memory': int, 'sections': dict[str, int]}
    """
    try:
        with open(elf_path, "rb") as f:
            elffile = ELFFile(f)

            sections = {}
            total_memory = 0

            for section in elffile.iter_sections():
                size = section.header.sh_size
                sections[section.name] = size
                total_memory += size

            return {"total_memory": total_memory, "sections": sections}
    except Exception as e:
        raise RuntimeError(f"Error analyzing ELF file {elf_path}: {e}")


def process_combination(bench_name, filename, board_name, env_entry, mappings):
    env_name = env_entry["name"]
    label = env_entry.get("label", env_name)
    env_vars = env_entry.get("env", {})
    print(f"\nProcessing {bench_name} on {board_name} with {label}...")

    env_dir = env_name
    if not os.path.isdir(env_dir):
        print(f"  [ERROR] Directory {env_dir} not found, skipping")
        return []

    try:
        symbols_file = run_make_cosy(env_dir, board_name, filename, env_vars)
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Error running make cosy-output: {e}")
        return []

    symbols_path = os.path.join(env_dir, symbols_file)
    if not os.path.exists(symbols_path):
        print("  [ERROR] symbols.json not found, skipping")
        return []

    try:
        with open(symbols_path) as f:
            data = json.load(f)
    except Exception as e:
        print(f"  [ERROR] Error reading symbols.json: {e}")
        return []

    cat_type_sizes = process_symbols(data['symbols'], mappings, board_name)

    elf_path = os.path.join(env_dir, "bin", board_name, f"{env_dir}_benchmark.elf")
    elf_sizes = analyze_elf_sizes(elf_path)

    results = []
    for (cat, stype), size in cat_type_sizes.items():
        total_size = elf_sizes["total_memory"]
        section_total_size = elf_sizes["sections"].get(stype.section)

        results.append(
            {
                "benchmark": bench_name,
                "board": board_name,
                "environment": label,
                "category": cat,
                "type": stype.section,
                "size": size,
                "total_size": total_size,
                "section_total_size": section_total_size,
            }
        )

    # Delete symbols.json
    try:
        os.remove(symbols_path)
    except Exception as e:
        print(f"  [WARNING] Error deleting symbols.json: {e}")

    return results


def write_csv(results, out_path):
    try:
        os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
        with open(out_path, 'w', newline='') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "benchmark",
                    "board",
                    "environment",
                    "category",
                    "type",
                    "size",
                    "total_size",
                    "section_total_size",
                ],
            )
            writer.writeheader()
            writer.writerows(results)
        print(f"Results written to {out_path}")
    except Exception as e:
        raise RuntimeError(f"Error writing CSV: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Measure static memory sizes using cosy tool')
    parser.add_argument('--config', default='benchmark-config.yml',
                        help='Path to benchmark config YAML file')
    parser.add_argument('--mappings', help='YAML file with category mappings')
    parser.add_argument('--output', default='./memory-sizes.csv',
                        help='Path to write the memory sizes CSV (default: ./memory-sizes.csv)')
    args = parser.parse_args()

    try:
        mappings = load_mappings(args.mappings)
        config = Config.from_yml(args.config)
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    results = []

    for bb in config.benchmarks:
        bench_name = bb.name
        filename = bb.filename
        board_name = bb.board_name

        for env_entry in bb.supported_environments:
            disabled = env_entry.get('disabled', False)
            if disabled:
                continue

            combo_results = process_combination(
                bench_name, filename, board_name, env_entry, mappings
            )
            results.extend(combo_results)

    try:
        write_csv(results, args.output)
        print("All processing complete!")
    except RuntimeError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
