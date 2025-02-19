# Root Makefile

.DEFAULT_GOAL := all

# Variables
BACKEND_DIR := backend
NO_PRINT_FLAG := --no-print-directory

# Include backend Makefile
include $(BACKEND_DIR)/Makefile

.PHONY: backend-delete-venv
backend-delete-venv:
	@ $(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) delete_venv

.PHONY: backend-format
backend-format:
	@ $(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) format

.PHONY: backend-lint
backend-lint:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) lint

.PHONY: backend-type-check
backend-type-check:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) type-check

.PHONY: backend-jupyter
backend-jupyter:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) jupyter

.PHONY: backend-test
backend-test:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) test

.PHONY: backend-run-dev-server
backend-run-dev-server:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) run-dev-server

.PHONY: backend-run-server
backend-run-server:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) run-server

.PHONY: backend-clean
backend-clean:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) clean

.PHONY: backend-all
backend-all:
	@$(MAKE) -C $(BACKEND_DIR) $(NO_PRINT_FLAG) all

.PHONY: frontend-run-dev-server
frontend-run-dev-server:
	@npm run dev --prefix ./frontend

.PHONY: frontend-install
frontend-install:
	@npm install --prefix ./frontend

.PHONY: frontend-format
frontend-format:
	@npm run format --prefix ./frontend

.PHONY: frontend-lint
frontend-lint:
	@npm run lint --prefix ./frontend

.PHONY: frontend-test
frontend-test:
#	@npm run test --prefix ./frontend
	@echo "TODO: Add frontend tests"

.PHONY: frontend-all
frontend-all: frontend-install frontend-format frontend-test
