SHELL:=/bin/bash
WELLIES_VERSION = 1.0.1.dev1+g02bc81e

user:
	module load wellies/1.0.0; \
	module list; \
	./deploy.py configs_fdb_dev/config.yaml configs_fdb_dev/data.yaml configs_fdb_dev/execution_contexts.yaml configs_fdb_dev/tools.yaml ${ARGS}

local:
	./deploy.py configs/config.yaml configs/data.yaml configs/execution_contexts.yaml configs/tools.yaml ${ARGS}
default: user
