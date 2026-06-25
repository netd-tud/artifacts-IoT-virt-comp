RIOTBASE ?= $(CURDIR)/../../RIOT

SCALE_FACTOR ?= 1
HEAP_SIZE ?= 0

# export EXTRA_CFLAGS += -Os -emit-llvm -DSCALE_FACTOR=$(SCALE_FACTOR)
export EXTRA_CFLAGS += -fno-builtin-memcpy -fno-builtin-memset -Os -DSCALE_FACTOR=$(SCALE_FACTOR) -DHEAP_SIZE=$(HEAP_SIZE)

include $(RIOTBASE)/makefiles/rbpf.inc.mk

.PHONY: all test

test:
	echo $(RBPF_SOURCES)

RBPF_INCLUDE += -I$(CURDIR)/helpers.h
# Default FILE to ../benchmark (so dump uses ../benchmark.bin by default)

DUMP_FILE ?= ../benchmark

dump:
	$(RBPF_GENRBF) dump $(DUMP_FILE).bin
