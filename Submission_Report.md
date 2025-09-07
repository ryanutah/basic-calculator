# Open-Source Contribution Report — Basic Calculator (Python)
**Date:** September 07, 2025  

## Project Overview
**Repo:** `AgyeyaMishra/basic-calculator`  
**Description:** A simple Python calculator performing addition, subtraction, multiplication, and division for two numbers.  
**Why this project:** Small, approachable codebase aligned to my early‑career Python goals and perfect for practicing OSS workflow.  

## Development Setup
1. Fork the repository on GitHub and clone your fork.
2. Create a virtual environment and install dev deps:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run tests and lints:
   ```bash
   pytest -q
   ruff check .
   black --check .
   ```
**Dependencies:** Python 3.8+; dev tools: pytest, ruff, black.  

## Work Item Selection
**Chosen item:** Add a robust CLI, improve input validation (including numeric strings), handle divide‑by‑zero explicitly, add pytest coverage, and set up CI.  
**Rationale:** Improves usability (non‑interactive usage), safety (clear errors), maintainability (tests), and contributor experience (CI).  

## Implementation Summary
- `Functions.py`: type validation helper (`_to_number`), clearer error messages, `ZeroDivisionError` on `/0`.
- `BasicCalculator.py`: argparse CLI with `--interactive` option.
- `tests/test_calculator.py`: unit tests for success and error paths.
- Tooling: `pyproject.toml` for Ruff/Black; GitHub Actions workflow for CI; `requirements.txt`.
- Docs: README additions and PR template.

## Pre‑Checkin Checks & Code Review
- Ran `ruff` and `black --check` locally.
- Executed `pytest` to ensure all tests pass.
- Opened a pull request to the upstream repo.
- _Reviewer:_ **Maintainer(s)** of the repo.  
- _Review process:_ PR created with description; addressed any feedback by pushing fixup commits.  

> **Screenshot placeholders:**  
> 1) Terminal: tests and lints passing.  
> 2) PR page with description.  
> 3) GitHub Actions CI run green.

## Testing & (If Applicable) Deployment
- **Automated tests:** `pytest` unit tests introduced in this contribution.
- **Manual testing:** Verified CLI behavior in interactive and non-interactive modes.
- **Deployment:** Not applicable; this is a Python script library. CI ensures regressions are caught on PRs.

## Impact of the Change
- **Reliability:** Explicit exceptions; validated inputs reduce silent failures.
- **Usability:** Script‑friendly CLI and interactive prompt.
- **Contributor UX:** CI and formatting unify contributions and reduce review time.
- **Alignment:** Enhances the educational value and robustness of a beginner project.

## Use‑Cases & Requirements
### User Stories
1. **As a** user, **I want** to call the calculator from the shell with two operands **so that** I can use it in scripts.  
2. **As a** beginner, **I want** clear errors on invalid input **so that** I can correct mistakes quickly.  
3. **As a** maintainer, **I want** automated tests and linting **so that** contributions remain high quality.

### Use‑Case Diagram (textual)
_Actors:_ User, Maintainer, CI  
_Use‑Cases:_ Run Operation, See Error, Run Tests, Review PR, CI Lint/Test  
_Relationships:_ User -> Run Operation; Run Operation -> (includes) Validate Inputs; Maintainer -> Review PR; CI -> (automates) Lint & Test on PR.

### Minimal ER‑like Model (conceptual)
- **Operation**(name, function) — four rows: add, subtract, multiply, divide  
- **Invocation**(op_name, a, b, result, error?) — produced by CLI runs  
- **TestCase**(name, expects_error?, expected_value) — executed by pytest

## How to Reproduce Locally
```bash
git clone <your-fork-url>
cd basic-calculator
# copy contents of this pack over the repo root (or cherry-pick files)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python src/BasicCalculator.py add 2 3
python src/BasicCalculator.py --interactive
```

## Links
- **Repository:** https://github.com/AgyeyaMishra/basic-calculator
- **Your PR:** _Insert URL here after opening the PR._

---

_Appendix: Commands_  
```bash
git checkout -b feat/cli-validation-tests
# copy files from this pack into the repo (preserve paths)
git add .
git commit -m "feat: argparse CLI, input validation, tests, CI, and tooling"
git push -u origin feat/cli-validation-tests
# open PR on GitHub and paste the PR template from PULL_REQUEST_TEMPLATE.md
```
