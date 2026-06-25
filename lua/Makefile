APPLICATION = lua_benchmark

# If no BOARD is found in the environment, use this default:
BOARD ?= native

# This has to be the absolute path to the RIOT base directory:
RIOTBASE ?= $(CURDIR)/../RIOT

# Comment this out to disable code in RIOT that does safety checking
# which is not needed in a production environment but helps in the
# development process:
DEVELHELP ?= 1

# Change this to 0 show compiler invocation lines by default:
QUIET ?= 1

USEPKG += lua
USEPKG += mpaland-printf

USEMODULE += ztimer_usec

ifeq ($(MEASURE_MALLOC), ON)
USEMODULE += malloc_monitor
CFLAGS += -DMEASURE_MALLOC
endif

# generate .lua.h header files of .lua files
BENCHMARK ?= tarfind
BENCHMARK_FILE = benchmarks/$(BENCHMARK).lua
ITERATIONS ?= 1
SCALE_FACTOR ?= 1
MEM_STATS ?= OFF
GC_AGGRESSIVE ?= OFF
DUMP_OPCODES ?= OFF
MATH ?= OFF
STRING ?= OFF
TABLE ?= OFF

CFLAGS += -DBENCH_ITERATIONS=$(ITERATIONS)

# Lua has a riot stack and a heap. For each function call it allocates a stack
# on its own heap.
RIOT_STACK ?= 4096
HEAP ?= 65536

CFLAGS += -DTHREAD_STACKSIZE_MAIN=$(RIOT_STACK)
CFLAGS += -DLUA_MEM_SIZE=$(HEAP)

ifeq ($(DUMP_OPCODES), ON)
  CFLAGS += -DDUMP_OPCODES
endif

ifeq ($(MEM_STATS), ON)
  CFLAGS += -DMEM_STATS
endif

ifeq ($(GC_AGGRESSIVE), ON)
  CFLAGS += -DGC_AGGRESSIVE
endif

ifeq ($(MATH), ON)
  CFLAGS += -DLOAD_MATH
endif

ifeq ($(STRING), ON)
  CFLAGS += -DLOAD_STRING
endif

ifeq ($(TABLE), ON)
  CFLAGS += -DLOAD_TABLE
endif

ifeq ($(BIGINT), ON)
	CFLAGS += -DLUA_64BITS
endif

all: benchmark.lua

.PHONY: .FORCE

benchmark.lua: .FORCE
	cp $(BENCHMARK_FILE) benchmark.lua
	sed -i "s/SCALE_FACTOR = .*/SCALE_FACTOR = $(SCALE_FACTOR);/" benchmark.lua
	@grep "SCALE_FACTOR =" benchmark.lua

BLOBS += benchmark.lua

include $(RIOTBASE)/Makefile.include

include ../Makefile.include
