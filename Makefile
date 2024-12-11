

.DEFAULT_GOAL := help


.PHONY : help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


# Install requirements
.PHONY : install
install: ## Install dependencies for production
	python3 -m pip --require-virtualenv install --upgrade pip
	python3 -m pip --require-virtualenv install flit build
	python3 -m flit install --deps production
	python3 -m pip --require-virtualenv install .

.PHONY : install-dev
install-dev: install ## Install dependencies for development and production
	python3 -m pip --require-virtualenv install '.[dev]'
	pre-commit install --hook-type pre-commit --hook-type pre-push

# Build and upload package
.PHONY : build
build: ## Build python package
	python3 -m build
	python3 -m twine check --strict dist/*.whl

.PHONY : upload
upload: ## Publish package with flit
	python3 -m flit publish

# Testing
.PHONY : pytest
pytest: ## Run pytest with coverage
	python3 -m coverage run -m pytest --maxfail=10
	python3 -m coverage report -m
	python3 -m coverage html

uninstall: ## Uninstall package
	python3 -m pip uninstall matplotlib_sankey -y --quiet


reinstall: uninstall ## Uninstall and install package
	python3 -m pip --require-virtualenv install .


format: ## Formatting code
	isort matplotlib_sankey/*.py
	isort tests/*.py

freeze: ## Freeze dependencies
	python3 --version > .python-version
	python3 -m pip freeze --exclude matplotlib_sankey > requirements.txt

typing: ## Check typing of code with mypy
	python3 -m mypy matplotlib_sankey/*.py


check: install-dev freeze format typing pytest build ## Running all checks
