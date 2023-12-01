# advent_of_code_2023
My 2023 Advent of code solutions

## Installation
- Prerequisites: Docker, Git
- Clone the repo
- `cd advent_of_code_2023`
- `make install` to install virtual environment and dependencies
- `source .venv/bin/activate` to source the virtual environment (installed at the previous step)
- `pre-commit install` to initialise pre-commit (for code quality checks to run before each commit). To disable it, just add `--no-verify`` after the commit (example: `git commit -a -m "<commit-message>" --no-verify`).
- `make run` to launch the main script
