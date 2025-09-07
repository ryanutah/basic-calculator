### Summary
Add argparse-based CLI, stronger input validation, tests, and CI to improve reliability and usability.

### Motivation
- Current repo offers basic functions but no non-interactive CLI, limited validation, and minimal tests.
- This PR brings safer behavior (explicit ZeroDivisionError), improves DX, and sets up CI for contributors.

### Changes
- `Functions.py`: validate inputs; support numeric strings; raise ZeroDivisionError for /0.
- `BasicCalculator.py`: argparse CLI + `--interactive` prompt mode.
- `tests/test_calculator.py`: unit tests for all operations, error paths.
- `pyproject.toml`: Ruff & Black config.
- `.github/workflows/ci.yml`: CI for lint & tests.
- `requirements.txt`: add dev deps.
- `README`: usage examples and setup (see diff).

### Pre‑checkin
- `ruff check .` passes
- `black --check .` passes
- `pytest` green locally

### Screenshots
_Add any terminal output screenshots (tests passing, CLI usage), and the Actions run badge once merged._

### Notes
Backwards compatible for code importers; only behavioral change is explicit exception on divide-by-zero.
