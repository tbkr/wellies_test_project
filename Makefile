SHELL:=/bin/bash
WELLIES_VERSION = 1.0.1.dev1+g02bc81e

user:
	module load wellies/$(WELLIES_VERSION); \
	module list; \
	./deploy.py configs/config.yaml configs/data.yaml configs/execution_contexts.yaml configs/tools.yaml ${ARGS}

local:
	./deploy.py configs/config.yaml configs/data.yaml configs/execution_contexts.yaml configs/tools.yaml ${ARGS}
default: user
