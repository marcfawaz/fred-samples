TARGET  := $(CURDIR)/target
VENV    := $(CURDIR)/.venv
PYTHON  := $(VENV)/bin/python
PIP     := $(VENV)/bin/pip
UV      := $(VENV)/bin/uv

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

# ── Bootstrap ──────────────────────────────────────────────────────────────────

$(TARGET)/.venv-created:
	@mkdir -p $(TARGET)
	python3 -m venv $(VENV)
	@touch $@

$(TARGET)/.uv-installed: $(TARGET)/.venv-created
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install uv
	@touch $@

$(TARGET)/.compiled: pyproject.toml $(TARGET)/.uv-installed
	$(UV) sync --extra dev
	@touch $@

.PHONY: dev
dev: $(TARGET)/.compiled ## Install dependencies
	@echo "✅ Dependencies installed."

# ── Main targets ───────────────────────────────────────────────────────────────

.PHONY: run
run: dev ## Start the sample agents pod locally
	ENV_FILE=$(CURDIR)/config/.env VIRTUAL_ENV= $(UV) run python -m fred_samples_agents

.PHONY: chat
chat: dev ## Open the interactive chat client for a running pod
	VIRTUAL_ENV= $(UV) run fred-agent-chat

.PHONY: update
update: $(TARGET)/.uv-installed ## Re-resolve and update all dependencies
	$(UV) sync
	@touch $(TARGET)/.compiled

.PHONY: lint
lint: dev ## Run ruff linter
	$(UV) run ruff check fred_samples_agents/

.PHONY: clean
clean: ## Remove the virtual environment and cached files
	rm -rf $(VENV) $(TARGET)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
