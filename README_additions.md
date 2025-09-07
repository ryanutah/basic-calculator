# Contribution: safer CLI, tests, CI

This change adds:
- A robust CLI (`BasicCalculator.py`) with argparse and an optional `--interactive` mode.
- Safer operations in `Functions.py` (type validation; clear ZeroDivisionError).
- Pytest coverage in `tests/test_calculator.py`.
- Ruff + Black configuration via `pyproject.toml`.
- GitHub Actions workflow for linting and tests.

## Local Dev Setup

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python src/BasicCalculator.py add 2 3
python src/BasicCalculator.py --interactive
```

