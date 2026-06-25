#!/usr/bin/env python3

# A benchmark is represented by the Benchmark class. This class contains
# information like the board, benchmark name (and path),
# and the default environment variables.
# The ExecutionStrategy list defines how the benchmark is exeucted.
# The BinarySearchExecutionStrategy executes a benchmark repreatedly
# while adjusting an environment variable to find a minimum.
# The IncrementalExecutionStrategy executes a benchmark repreatedly while
# adjusting one environment variable in fixed steps and records the runtime.
# The RegularExecutionStrategy just executes a benchmark
# and parses its output.


from config import Config
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple
import os
import time
import sys
import math
import csv
import datetime
import argparse
import serial


class FlashError(Exception):
    pass


class RunError(Exception):
    pass


class Benchmark:
    START_MARKER = "=== Benchmark Begins ==="
    END_MARKER = "=== Benchmark End ==="
    FAIL_MARKERS = [
        "error", "Error", "not enough memory", "exit 10:",
        "MemoryError", "Script execution error", "Exception",
        "failed", "false", "hardfault", "panic"
    ]

    def __init__(self, name: str, folder: str, environment: str, board: str,
                 scale_factor: int, iterations: int, env: Dict[str, str],
                 inter_line_timeout: int = 9, total_timeout: int = 180) -> None:
        self.name = name
        self.folder = folder
        self.environment = environment
        self.board = board
        self.scale_factor = scale_factor
        self.iterations = iterations
        self.env = env
        self.inter_line_timeout = inter_line_timeout
        self.total_timeout = total_timeout

    def __str__(self) -> str:
        return f"{self.name} for {self.environment}"

    def build_env(self, env_override: Dict[str, str] = None) -> Dict[str, str]:
        sys_env = os.environ.copy()
        command_env = {
            "BOARD": self.board,
            "BENCHMARK": self.name,
            "SCALE_FACTOR": str(self.scale_factor),
            "ITERATIONS": str(self.iterations),
            **self.env
        }
        command_env = sys_env | command_env
        if env_override:
            command_env.update(env_override)
        return command_env

    def flash(self, env_override: Dict[str, str] = None):
        command_env = self.build_env(env_override)
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
            raise FlashError(
                f"Flashing failed with error {flash_process.returncode}!\n"
                f"STDOUT:\n{flash_process.stdout}\nSTDERR:\n{flash_process.stderr}"
            )

    def run(self, env_override: Dict[str, str] = None):
        output = ""
        success = True
        started = False

        # each benchmark waits at least 3 seconds before starting anyway.
        time.sleep(1)

        ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=0.01)
        ser.reset_input_buffer()  # Clear any stale data

        start = time.monotonic()
        end = start + self.total_timeout
        next_deadline = start + self.inter_line_timeout

        try:
            while True:
                t = time.monotonic()
                if t >= next_deadline or t >= end:
                    success = False
                    if started:
                        print("timed out - ", end="")
                    else:
                        print(f"no start marker after {self.inter_line_timeout} seconds -", end="")
                    break

                raw_line = ser.readline()
                if not raw_line:
                    continue

                line = raw_line.decode("utf-8", errors="replace")
                if self.START_MARKER in line:
                    started = True
                if not started:
                    continue
                # We only adjust the next_deadline if the benchmark already has started.
                # If not and it takes longer than inter_line_timeout seconds we fail.
                next_deadline = t + self.inter_line_timeout
                output += line

                if any(marker in line for marker in self.FAIL_MARKERS):
                    time.sleep(0.25)
                    while ser.in_waiting:
                        output += ser.readline().decode("utf-8", errors="replace")
                    success = False
                    break
                if self.END_MARKER in line:
                    break
        finally:
            ser.close()

        return (success, output)

    def parse_bench(self, stdout: str) -> List[Dict]:
        start_idx = stdout.index(self.START_MARKER) + len(self.START_MARKER)
        end_idx = stdout.index(self.END_MARKER)
        assert end_idx is not None and start_idx is not None, "The output passed to parse_bench is incomplete!"
        bench_output = stdout[start_idx:end_idx].strip()

        lines = []
        for line in bench_output.split("\n"):
            line = line.strip()
            if "# " in line:
                line = line.split("# ", 1)[1]
            lines.append(line)

        header = lines[0].split(";")
        results = []
        for line in lines[1:]:
            if not line:
                continue
            values = line.split(";")
            row = {}
            for key, val in zip(header, values):
                row[key] = val
            results.append(row)
        return results

    def execute_strategies(self, execution_strategies: List['ExecutionStrategy']) -> List[Dict]:
        results = []
        base_info = {
            "benchmark": self.name,
            "board": self.board,
            "environment": self.environment,
            "scale_factor": self.scale_factor,
            "iterations": self.iterations,
        }
        for strategy in execution_strategies:
            strategy_results = strategy.execute(self)
            for i, res in enumerate(strategy_results):
                if i >= len(results):
                    # first result
                    results.append(base_info.copy())
                # add our value to the result
                results[i].update(res)
        return results


def parse_config(config_file: str) -> 'Config':
    return Config.from_yml(config_file)


class ExecutionStrategy:

    def execute(self, benchmark: 'Benchmark') -> List[Dict]:
        pass


class RegularExecutionStrategy(ExecutionStrategy):
    def __init__(self) -> None:
        pass

    def execute(self, benchmark: 'Benchmark') -> List[Dict]:
        results = []

        print(f'Flashing {benchmark} - ', end="")
        sys.stdout.flush()
        benchmark.flash({})
        print('done - ', end="")
        sys.stdout.flush()

        success, stdout = benchmark.run({})
        if success:
            print("Parsed!")
            result = self.parse_output(benchmark, stdout)
            results.extend(result)
        else:
            raise RuntimeError(f"Failure while executing {benchmark}. ENV: {benchmark.build_env()}. STDOUT: {stdout}")
        return results

    def parse_output(self, benchmark: 'Benchmark', stdout: str) -> List[Dict]:
        return benchmark.parse_bench(stdout)


class TrackAllocationsExecutionStrategy(RegularExecutionStrategy):
    MEM_MARKER = "Dynamically allocated memory:"

    def parse_output(self, benchmark: 'Benchmark', stdout: str) -> List[Dict]:
        for line in stdout.split("\n"):
            if self.MEM_MARKER in line:
                am = int(line.split(self.MEM_MARKER)[1])
                return [{"allocated_memory": str(am)}]
        raise RuntimeError(f"{benchmark} did return the dynamically allocated memory!")


class IncrementalExecutionStrategy(ExecutionStrategy):
    def __init__(self, target_vari: str, start: int, step: int) -> None:
        self.target_vari = target_vari
        self.start = start
        self.step = step

    def execute(self, benchmark: 'Benchmark') -> List[Dict]:
        results = []
        current = self.start

        while current > 0:
            env_override = {
                self.target_vari: str(current),
            }

            print(f'Flashing {benchmark}({self.target_vari}={current}) - ', end="")
            sys.stdout.flush()
            benchmark.flash(env_override)
            print('done - ', end="")
            sys.stdout.flush()

            success, stdout = benchmark.run(env_override)
            if success:
                print(f"{self.target_vari}={current} runs")
                result = benchmark.parse_bench(stdout)
                for r in result:
                    # The benchmark does not print is heap or stack, so we add it to the result
                    r[self.target_vari.lower()] = current
                results.extend(result)
            else:
                print(f"{self.target_vari}={current} fails")
                print(f"STDOUT:\n{stdout.replace('\n', '\n\t')}")
                break
            sys.stdout.flush()
            current -= self.step

        sys.stdout.flush()
        if len(results) == 0:
            print(f"{benchmark} did not run for {self.target_vari}={current}")
        return results


class BinarySearchExecutionStrategy(ExecutionStrategy):
    def __init__(self, target_vari: str, start: int, end: int, precision: int) -> None:
        assert start < end
        self.target_vari = target_vari
        self.start = start
        self.end = end
        self.precision = precision

    def execute(self, benchmark: 'Benchmark') -> List[Dict]:
        low = self.start
        high = self.end
        last_successful_value = None

        while (high - low) >= self.precision and high > 1:
            mid = (low + high) // 2
            assert mid > 0

            env_override = {
                'ITERATIONS': '2',
                self.target_vari: str(mid),
            }

            print(f'Flashing {benchmark}({self.target_vari}={mid}) - ', end="")
            sys.stdout.flush()
            benchmark.flash(env_override)
            print('done - ', end="")
            sys.stdout.flush()

            success, stdout = benchmark.run(env_override)
            if success:
                print(f"{self.target_vari}={mid} runs")
                last_successful_value = mid
                high = mid
            else:
                print(f"{self.target_vari}={mid} fails")
                # print(f"ENV: {benchmark.build_env(env_override)}")
                # print(f"STDOUT:\n{stdout.replace('\n', '\n\t')}")
                low = mid + self.precision
            sys.stdout.flush()

        value = last_successful_value
        print(f"=== {benchmark} {self.target_vari}={value} ===")
        return [{self.target_vari.lower(): value}]


def gen_gc_pressure_benchmarks(config: 'Config') -> List[Tuple[Benchmark, List['ExecutionStrategy']]]:
    ben_exec_pairs = []
    projected_time = 0
    number_flashes = 0
    margin = 2.0
    for bench in config.benchmarks:
        print(f"Generating execution strategies for {bench.name} on a {bench.board_name}"
              " testing garbage collector pressure.")
        for se in bench.supported_environments:
            if se.get("name") not in ["jerryscript", "micropython", "lua"]:
                continue
            env = se.get("env", {})
            target_env = {**{k: str(v) for k, v in env.items()}}
            reduced_iterations = 8

            benchmark = Benchmark(
                name=bench.name,
                folder=str(Path(se.get("name"))),
                board="nrf52840dk",
                scale_factor=int(bench.scale_factor),
                iterations=reduced_iterations,
                environment=se.get("label", se.get("name")),
                env=target_env,
            )

            strategies = []

            if "HEAP" in env:
                step = 1 if se.get("name") == "jerryscript" else 1000
                max_heap = 180 if se.get("name") == "jerryscript" else 180_000
                # The heap value already has a 10% margin increase it to 100%
                start = min(int(target_env["HEAP"]) / 1.1 * margin, max_heap)
                projected_n = math.ceil((start - start / margin)/step)
                # 30 seconds flashing + 16 seconds reading times the number of steps
                projected_time += projected_n * (30 + 16)
                number_flashes += projected_n
                strategies.append(IncrementalExecutionStrategy("HEAP", math.ceil(start), step))

            ben_exec_pairs.append((benchmark, strategies))

    print(f"Projected runtime: {datetime.timedelta(seconds=projected_time)} ({number_flashes} flashes)")
    return ben_exec_pairs


def gen_limit_benchmarks(config: 'Config') -> List[Tuple[Benchmark, List['ExecutionStrategy']]]:
    ben_exec_pairs = []
    projected_time = 0
    number_flashes = 0
    for bench in config.benchmarks:
        print(f"Generating execution strategies for {bench.name} on a {bench.board_name}"
              " testing the limits for HEAP, STACK, and RIOT_STACK.")
        for se in bench.supported_environments:
            env = se.get("env", {})
            target_env = {**{k: str(v) for k, v in env.items()}}

            benchmark = Benchmark(
                name=bench.name,
                folder=str(Path(se.get("name"))),
                board="nrf52840dk",
                scale_factor=int(bench.scale_factor),
                iterations=2,
                environment=se.get("label", se.get("name")),
                env=target_env,
            )

            strategies = []

            for target_vari in ["HEAP", "STACK"]:
                if target_vari not in env:
                    continue
                end = int(target_env[target_vari])
                # jerryscript uses kB instead of bytes -> give it an additional margin
                if end < 500:
                    end += 3
                precision = 1 if end < 500 else 100
                strategies.append(BinarySearchExecutionStrategy(target_vari, 0, end, precision))
                # (30 seconds compiling and flashing + 16 seconds reading) * complexity of our search
                projected_time += (30 + 16) * math.ceil(math.log(end // precision))
                number_flashes += math.ceil(math.log2(end // precision))

            if "RIOT_STACK" in env:
                end = int(target_env["RIOT_STACK"])
                strategies.append(BinarySearchExecutionStrategy("RIOT_STACK", 0, end, 100))
                # (30 seconds compiling and flashing + 16 seconds reading) * complexity of our search
                projected_time += (30 + 16) * math.ceil(math.log(end // 100))
                number_flashes += math.ceil(math.log2(end // 100))

            ben_exec_pairs.append((benchmark, strategies))

    print(f"Projected runtime: {datetime.timedelta(seconds=projected_time)} ({number_flashes} flashes)")
    return ben_exec_pairs


def gen_runtime_benchmarks(config: 'Config') -> List[Tuple[Benchmark, List['ExecutionStrategy']]]:
    ben_exec_pairs = []
    number_flashes = 0
    for bench in config.benchmarks:
        print(f"Generating execution strategies for {bench.name} on a {bench.board_name}"
              " tracking their runtime.")
        for se in bench.supported_environments:
            env = se.get("env", {})
            target_env = {
                **{k: str(v) for k, v in env.items()}
            }
            benchmark = Benchmark(
                name=bench.name,
                folder=str(Path(se.get("name"))),
                board="nrf52840dk",
                scale_factor=int(bench.scale_factor),
                iterations=int(bench.iterations),
                environment=se.get("label", se.get("name")),
                env=target_env,
            )
            strategies = [RegularExecutionStrategy()]
            ben_exec_pairs.append((benchmark, strategies))
    number_flashes = len(ben_exec_pairs)
    print(f"Projected runtime: {datetime.timedelta(seconds=number_flashes * 40)} ({number_flashes} flashes)")
    return ben_exec_pairs


def gen_allocations_benchmarks(config: 'Config') -> List[Tuple[Benchmark, List['ExecutionStrategy']]]:
    ben_exec_pairs = []
    for bench in config.benchmarks:
        print(f"Generating execution strategies for {bench.name} on a {bench.board_name}"
              " tracking their runtime.")
        for se in bench.supported_environments:
            env = se.get("env", {""})
            if se.get("name") not in ["micro-bpf", "wamr"]:
                continue
            target_env = {
                "MEASURE_MALLOC": "ON",
                **{k: str(v) for k, v in env.items()}
            }
            benchmark = Benchmark(
                name=bench.name,
                folder=str(Path(se.get("name"))),
                board="nrf52840dk",
                scale_factor=int(bench.scale_factor),
                iterations=int(bench.iterations),
                environment=se.get("label", se.get("name")),
                env=target_env,
            )
            strategies = [TrackAllocationsExecutionStrategy()]
            ben_exec_pairs.append((benchmark, strategies))
    number_flashes = len(ben_exec_pairs)
    print(f"Projected runtime: {datetime.timedelta(seconds=number_flashes * 40)} ({number_flashes} flashes)")
    return ben_exec_pairs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["gc_pressure", "limit", "runtime", "alloc"])
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    config = parse_config(args.config)
    if args.command == "gc_pressure":
        ben_exec_pairs = gen_gc_pressure_benchmarks(config)
    elif args.command == "limit":
        ben_exec_pairs = gen_limit_benchmarks(config)
    elif args.command == "runtime":
        ben_exec_pairs = gen_runtime_benchmarks(config)
    elif args.command == "alloc":
        ben_exec_pairs = gen_allocations_benchmarks(config)
    output = []
    for benchmark, exec_strats in ben_exec_pairs:
        output.extend(benchmark.execute_strategies(exec_strats))

    keys = list(dict.fromkeys(k for o in output for k in o.keys()).keys())
    with open(args.output, "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote output to {args.output}")


if __name__ == "__main__":
    main()
