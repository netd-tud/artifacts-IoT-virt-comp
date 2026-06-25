CONFIG_DIR := ./configs
MEMORY_DIR := ./data/memory
RUNTIME_DIR := ./data/runtime

.DEFAULT_GOAL := all

$(CONFIG_DIR)/nrf-config-limited.yaml: $(CONFIG_DIR)/nrf-config.yaml
	./scripts/run_script.py limit --config $< --output $(CONFIG_DIR)/memory_requirements.csv
	cp $< $@
	./scripts/update_config.py csv --source $(CONFIG_DIR)/memory_requirements.csv --output $@ --margin 1.1

$(MEMORY_DIR)/dynamic_memory.csv: $(CONFIG_DIR)/nrf-config-limited.yaml
	./scripts/run_script.py alloc --config $< --output $@

$(MEMORY_DIR)/section_sizes.csv: $(CONFIG_DIR)/nrf-config-limited.yaml
	./scripts/run_memory.py --config $< --output $@ --mappings scripts/symbol-mappings.yml

$(RUNTIME_DIR)/gc_pressure_runtime.csv: $(CONFIG_DIR)/nrf-config-limited.yaml
	./scripts/run_script.py gc_pressure --config $< --output $@

$(RUNTIME_DIR)/bench_runtime.csv: $(CONFIG_DIR)/nrf-config-limited.yaml
	./scripts/run_script.py runtime --config $< --output $@

clean-config:
	rm -f $(CONFIG_DIR)/nrf-config-limited.yaml
	rm -f $(CONFIG_DIR)/memory_requirements.csv

clean-dynamic-memory:
	rm -f $(MEMORY_DIR)/dynamic_memory.csv

clean-section-sizes:
	rm -f $(MEMORY_DIR)/section_sizes.csv

clean-gc-pressure:
	rm -f $(RUNTIME_DIR)/gc_pressure_runtime.csv

clean-runtime-nrf:
	rm -f $(RUNTIME_DIR)/bench_runtime.csv

clean-mem: clean-dynamic-memory clean-section-sizes

clean-runtime: clean-runtime-nrf clean-gc-pressure

mrproper: clean-config clean-mem clean-runtime
	@echo "All generated files have been cleaned."

jupyter: $(MEMORY_DIR)/section_sizes.csv $(MEMORY_DIR)/dynamic_memory.csv $(RUNTIME_DIR)/gc_pressure_runtime.csv $(RUNTIME_DIR)/bench_runtime.csv
	cd ./analysis; \
	jupyter lab

all: jupyter

debug:
	./scripts/run_script.py runtime --config $(CONFIG_DIR)/nrf-config-debug.yaml --output /tmp/runtime.csv
