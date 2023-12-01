SHELL := /bin/bash
SRC := src

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all install run deploy down mypy fmt fmtcheck lint

all: install run

install:
	pip install --upgrade pip
	pip install poetry
	poetry install

fmt:
	poetry run isort $(SRC)
	poetry run black $(SRC)

fmtcheck:
	poetry run isort --check-only $(SRC)
	poetry run black --diff --check $(SRC)

lint:
	poetry run flake8 $(SRC)

run:
	PYTHONPATH=. poetry run python src/main.py

clean:
	@find . -name '__pycache__' -exec rm -rf {} \;
