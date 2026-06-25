#!/bin/bash

# This is a quick check I use the estimate how many of the instructions in this
# benchmark are 32 bit shifts.

BENCHMARK=nsichneu BOARD=nrf52840dk ITERATIONS=32 SCALE_FACTOR=1 RIOT_STACK=3750 make benchmark.o
echo "number of instructions:"
llvm-objdump --no-show-raw-insn --no-leading-addr -d benchmark.o | grep -e '\s' | wc -l
echo "number of <<= 32 or >>= 32 instructions:"
llvm-objdump --no-show-raw-insn --no-leading-addr -d benchmark.o | grep -e '\s' | grep '<<= 32\|>>= 32' | wc -l
