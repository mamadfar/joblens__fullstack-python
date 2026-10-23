.PHONY: help install fmt lint typecheck test check hooks

help: ## Show available targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-10s %s\n", $$1, $$2}'

install: ## Install deps from uv.lock
	uv sync

fmt: ## Auto-fix lint and format code
	uv run ruff check --fix
	uv run ruff format

lint: ## Check lint + formatting (no changes)
	uv run ruff check
	uv run ruff format --check

typecheck: ## Run mypy strict
	uv run mypy

test: ## Run tests
	uv run pytest

check: lint typecheck test ## Everything CI runs

hooks: ## Install git hooks and run them on all files
	uv run pre-commit install
	uv run pre-commit run --all-files
