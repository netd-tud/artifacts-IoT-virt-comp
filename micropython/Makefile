APPLICATION = micropython_benchmark

BOARD ?= native

RIOTBASE ?= $(CURDIR)/../RIOT

# USEPKG += micropython-local
USEPKG += micropython
USEMODULE += ztimer_usec
USEPKG += mpaland-printf

ifeq ($(MEASURE_MALLOC), ON)
USEMODULE += malloc_monitor
CFLAGS += -DMEASURE_MALLOC
endif

BENCHMARK ?= tarfind
BENCHMARK_FILE = benchmarks/$(BENCHMARK).py
ITERATIONS ?= 1
SCALE_FACTOR ?= 1
MEM_STATS ?= OFF

BLOBS += benchmark.py

# micropython does not have its own stack but shares one with RIOT.
# It defines a heap.
RIOT_STACK ?= 9192
HEAP ?= 65536

CFLAGS += -DTHREAD_STACKSIZE_MAIN=$(RIOT_STACK)
MP_RIOT_HEAPSIZE = $(HEAP)

# MicroPython needs a larger stack
CFLAGS += -DBENCH_ITERATIONS=$(ITERATIONS)
CFLAGS += -DMICROPY_NLR_SETJMP=1
ifeq ($(BIGINT), ON)
CFLAGS += -DMICROPY_LONGINT_IMPL=MICROPY_LONGINT_IMPL_MPZ
endif
# ifeq ($(MEM_STATS), ON)
# 	CFLAGS += -DMICROPY_MEM_STATS=1 -DMICROPY_MALLOC_USES_ALLOCATED_SIZE=1
# endif

# use miniterm (instead of the default pyterm) in order to support control
# characters (CTRL-D ...)
# RIOT_TERMINAL ?= miniterm

all: benchmark.py

.PHONY: .FORCE

benchmark.py: .FORCE
	cp $(BENCHMARK_FILE) benchmark.py
	sed -i "s/SCALE_FACTOR = .*/SCALE_FACTOR = $(SCALE_FACTOR);/" benchmark.py
	@grep "SCALE_FACTOR =" benchmark.py
	@if [ "$(MEM_STATS)" = "ON" ]; then \
		sed -i "s/# import micropython/import micropython/" benchmark.py; \
		sed -i "s/# print(\"\")/print(\"\")/" benchmark.py; \
		sed -i "s/# micropython.mem_info()/micropython.mem_info()/" benchmark.py; \
	fi

flamegraph: all
	sudo /usr/lib/linux-tools-6.8.0-79/perf record -g -- $(ELFFILE)
	sudo chown georg-baer-dumont:georg-baer-dumont ./perf.data
	/usr/lib/linux-tools-6.8.0-79/perf script > out.perf
	stackcollapse-perf.pl out.perf > out.folded
	flamegraph.pl out.folded > benchmark.svg
	google-chrome benchmark.svg

include $(RIOTBASE)/Makefile.include

include ../Makefile.include
