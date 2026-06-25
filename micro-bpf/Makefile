# name of your application
APPLICATION = micro-bpf_benchmark

# TODO: Fix bug in docker image
# BOARD_BLACKLIST := native32 native64 native

# The name of crate (as per Cargo.toml package name, but with '-' replaced with '_')
#
# The presence of this triggers building Rust code contained in this
# application in addition to any C code.
APPLICATION_RUST_MODULE = micro_bpf

# If no BOARD is found in the environment, use this default:
BOARD ?= nrf52840dk

# This has to be the absolute path to the RIOT base directory:
RIOTBASE ?= $(CURDIR)/../RIOT

# Basic networking, and gcoap
USEMODULE += ztimer
USEMODULE += ztimer_usec

USEMODULE += random
USEMODULE += memarray

USEPKG += mpaland-printf

ifeq ($(MEASURE_MALLOC), ON)
USEMODULE += malloc_monitor
CARGO_OPTIONS += --features measure_malloc
endif

# Required to use the bpf global storage.
# USEMODULE += bpf
# USEMODULE += btree
# USEMODULE += memarray

FEATURES_REQUIRED += rust_target

BENCHMARK ?= crc_32
BENCHMARK_FILE = $(CURDIR)/ebpf/$(BENCHMARK).c
ITERATIONS ?= 5
ENABLE_JIT ?= 0
export ITERATIONS

# Comment this out to disable code in RIOT that does safety checking
# which is not needed in a production environment but helps in the
# development process:
DEVELHELP ?= 1

CARGO_OPTIONS += $(if $(filter 1, $(ENABLE_JIT)), --features jit)

BINARY_FILE = $(if $(filter 1, $(ENABLE_JIT)), benchmark.o, benchmark.bin)

DISABLE_MODULE += mpu_stack_guard
FEATURES_BLACKLIST += cortexm_mpu

all: $(BINARY_FILE)

.PHONY: benchmark.o benchmark.bin

benchmark.bin: $(BENCHMARK_FILE)
	$(MAKE) -C $(CURDIR)/ebpf all RBPF_SOURCES=$(BENCHMARK_FILE) HEAP_SIZE=$(HEAP_SIZE)
	cp $(CURDIR)/ebpf/$(BENCHMARK).bin $(CURDIR)/benchmark.bin
	cp $(CURDIR)/ebpf/$(BENCHMARK).o $(CURDIR)/benchmark.o
# TODO: Remove (currently the makefile from ebpf build all the .c file , However I used different SCALE_FACTOR per benchmark)
# this means, that I have to recompiler for every run and cannot keep intermediary .bin / .o files
	rm $(CURDIR)/ebpf/$(BENCHMARK).bin
	rm $(CURDIR)/ebpf/$(BENCHMARK).o

benchmark.o: $(BENCHMARK_FILE)
	$(MAKE) -C $(CURDIR)/ebpf all RBPF_SOURCES=$(BENCHMARK_FILE) HEAP_SIZE=$(HEAP_SIZE)
	cp $(CURDIR)/ebpf/$(BENCHMARK).o $(CURDIR)/benchmark.o
#	llvm-strip -d -R .BTF -R .BTF.ext -o $(CURDIR)/benchmark.o $(CURDIR)/benchmark.o
# TODO: Remove (currently the makefile from ebpf build all the .c file , However I used different SCALE_FACTOR per benchmark)
# this means, that I have to recompiler for every run and cannot keep intermediary .bin / .o files
	rm $(CURDIR)/ebpf/$(BENCHMARK).bin
	rm $(CURDIR)/ebpf/$(BENCHMARK).o

# Change this to 0 show compiler invocation lines by default:
QUIET ?= 1

# micro-bpf only has a riot stack. The 512 bytes stacks are allocated at runtime.
RIOT_STACK ?= 4096

CFLAGS += -DTHREAD_STACKSIZE_MAIN=$(RIOT_STACK)

include $(RIOTBASE)/Makefile.include
include ../Makefile.include
