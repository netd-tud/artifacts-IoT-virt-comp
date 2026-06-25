#!/usr/bin/env python3

from config import BenchmarkBoard, Config
import subprocess
from pathlib import Path
from typing import List, Dict, Self, Optional
import os
import sys
import csv
import re

class Benchmark:
    def __init__(self, name: str, folder: str, environment: str, board: str, scale_factor: int, env: Dict[str, str]) -> Self:
        self.name = name
        self.folder = folder
        self.environment = environment
        self.board = board
        self.scale_factor = scale_factor
        self.env = env

    def __str__(self) -> str:
        return f"{self.name} for {self.environment}"

    def run(self) -> Dict[str, Optional[int]]:
        res = None
        print(f"Tracking dynamic memory allocations for {self}")
        sys_env = os.environ.copy()

        command_env = {
            'BOARD': self.board,
            'BENCHMARK': self.name,
            'SCALE_FACTOR': str(self.scale_factor),
            **self.env
        }

        command_env = sys_env | command_env

        try:
            sys.stdout.flush()
            flash_process = subprocess.run(
                ['make', 'all', 'flash'],
                cwd=self.folder,
                env=command_env,
                capture_output=True,
                text=True,
                bufsize=1,
                start_new_session=True,
            )

            if flash_process.returncode != 0:
                print(f"STDOUT:\n\t{flash_process.stdout.replace("\n", "\n\t")}")
                print(f"STERR :\n\t{flash_process.stderr.replace("\n", "\n\t")}")
                raise RuntimeError(f"Flashing failed with error {flash_process.returncode}!")
            else:
                print('done flashing - ', end="")
            sys.stdout.flush()

            start_marker = "=== Benchmark Begins ==="
            end_marker = "=== Benchmark End ==="

            mem_marker = "Dynamically allocated memory:"

            fail_markers = [
                "error",
                "Error"
                "not enough memory",
                "exit 10:",
                "MemoryError",
                "Script execution error",
                "Exception",
                "failed",
                "false"
            ]

            sys.stdout.flush()
            process = subprocess.run(
                ['timeout', '16', 'picocom', '-b', '115200', '/dev/ttyACM0', '--quiet', '--echo'],
                cwd=self.folder,
                env=command_env,
                capture_output=True,
                text=True,
                bufsize=1,
                start_new_session=True,
            )
            print("done reading - ", end="")
            sys.stdout.flush()

            if start_marker in process.stdout and end_marker in process.stdout and not any([f in process.stdout for f in fail_markers]):
                for line in process.stdout.split("\n"):
                    if mem_marker in line:
                        dmem = re.findall(r"\d+", line)
                        assert len(dmem) == 1, f"More then one number on line {line}"
                        break
                res = int(dmem[0])
                print(f"{self} allocated {res} bytes of memory!")
            else:
                print(f"{self} fails!")
                res = None
            sys.stdout.flush()
        except Exception as e:
            raise e
        return res


def parse_config(config_file: str) -> 'Config':
    return Config.from_yml(config_file)


def gen_benchmarks(config: 'Config') -> List['Benchmark']:
    benchmarks = []
    for bench in config.benchmarks:
        print(f"Creating benchmark objects for {bench.name} on a {bench.board_name}")
        for se in bench.supported_environments:
            if se.get("name") not in ["micro-bpf", "wamr"]:
                continue
            env = se.get("env", {})
            target_env = {
                "MEASURE_MALLOC": "ON",
                **{k: str(v) for k, v in env.items()}
            }

            benchmarks.append(Benchmark(
                name=bench.name,
                folder=str(Path(se.get("name"))),
                board="nrf52840dk",
                scale_factor=int(bench.scale_factor),
                environment=se.get("label", se.get("name")),
                env=target_env,
            ))
    return benchmarks


if __name__ == "__main__":
    config = parse_config("nrf-config.yaml")
    output_path = "data/memory/dynamic_memory.csv"
    benchmarks = gen_benchmarks(config)
    print("Done generating benchmark configs...")
    output = []
    sys.stdout.flush()
    for bench in benchmarks:
        res = bench.run()
        output.append(
            {
                "benchmark": bench.name,
                "board": bench.board,
                "environment": bench.environment,
                "allocated_memory": res if res is not None else -1,
            }
        )
    with open(output_path, "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote output to {output_path}")
