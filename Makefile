# Makefile
.PHONY: install virtualenv ipython clean test watch pflake8 fmt

install:
	@echo "Hello installing"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython -i


lint:
	@.venv/bin/pflake8


fmt:
	@.venv/bin/autoflake --remove-all-unused-imports --recursive --in-place .
	@.venv/bin/isort .
	@.venv/bin/black .


test:
	@.venv/bin/pytest -v -s


watch:
	# @.venv/bin/ptw -- -v -s
	@ls **/*.py | entr pytest


testci:
	@.venv/bin/pytest -v --junitxml=result.xml


clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

 
