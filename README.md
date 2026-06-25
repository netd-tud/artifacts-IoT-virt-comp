# Artifacts for "Virtualization on Constrained IoT Devices: A Comparative Study"

This repository provides a reproducible pipeline for benchmarking and analyzing virtualization 
on constrained IoT devices.
The workflow is containerized, automates empirical parameter tuning, and produces 
runtime and memory artifacts.

## Requirements

- Possess a (nrf52840-dk)[https://www.nordicsemi.com/Products/Development-hardware/nRF52840-DK]
- Docker
- dialout group membership (debian)

## Quick Start

> [!CAUTION]
> Running the full pipeline will take around 17 hours and flash your board ~2000 times.
> gc_pressure_runtime.csv: ~9 hours and ~1200 flashes
> Stage 1: ~8 hours and ~900 flashes

To launch the artifact pipeline in the pre-configured Docker container, run:

```shell
docker compose run artifact-2054
```

To start the Jupyter notebook run:

```shell
make jupyter
```

## Workflow Overview

The pipeline consists of two sequential stages:
**Stage 1** - Generate Config:

- Purpose: Automatically determine the minimum viable values for `HEAP`, `STACK` and `RIOT_STACK`
  using binary search (100-byte precision).
- Output: Tuned configuration file for stage 2

**Stage 2** - Recording Data:

- Purpose: Executing all benchmarks and generate runtime and memory artifacts
- Output:
  - Runtime Artifacts:
    - `bench_runtime.csv`: Load and execution times for each benchmark in all environments
    - `gc_pressure_runtime.csv`: Load and execution time as te HEAP size is incrementally reduced
  - Memory Artifacts:
    - `section_sizes.csv`: Binary composition by symbols and sections
    - `dynamic_memory.csv`: Runtime heap allocations on the RIOT heap

## Viewing Results:

To start the Jupyter Lab server and rebuild any missing artifacts, run:

```shell
make jupyter
```

## Rerunning Parts

Use the following make targets to manage and rerun specific pipeline stages:

| Command              | Effect                                                                                |
| -------------------- | ------------------------------------------------------------------------------------- |
| `make clean-config`  | Removes Stage 1 configuration files; triggers a full rerun of all downstream targets. |
| `make clean-runtime` | Removes runtime measurement data.                                                     |
| `make clean-memory`  | Removes memory measurement data.                                                      |
| `make mrproper`      | Removes all collected data.                                                           |

After cleaning, run `make jupyter` to regenerate the affected artifacts.

## Internal Working

### Executing Benchmarks:

The `run_script.py` script has four modes:

| Mode          | Description                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| `runtime`     | Records benchmark load and execution times across all environments.                                         |
| `gc_pressure` | Record garbage collector pressure by reducing `HEAP` from 200% of minimum in 1000-byte steps until failure. |
| `limit`       | Uses binary search to find minimum `HEAP`, `STACK` and `RIOT_STACK` values (100-byte precision; Stage 1).   |
| `alloc`       | Measures dynamic memory allocation on the RIOT heap for µBPF and WAMR (MEASURE_MALLOC=ON).                  |

### Static Memory Analyzes:

The `run_memory.py` script builds benchmarks and analyzes their memory footprint using Cosy.
Cosy is a RIOT tool for binary analyzes which matches the symbols
from the compiler generated symbol table to their sections.
We categorize ROM and RAM into Application, OS, and Runtime.
The `symbol_mappings.csv` specifies which symbols belong to which category.
