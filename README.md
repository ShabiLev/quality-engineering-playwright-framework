# Quality Engineering Playwright Framework

A production-style reference framework for scalable browser Quality Engineering using **Python, Playwright and pytest**.

This public showcase is intentionally built with **synthetic targets and demo data only**. It demonstrates reusable architecture, test layering, evidence capture and CI quality gates without exposing private environments, credentials or customer data.

## What It Demonstrates

- Smoke, regression and end-to-end test organization
- Page Object and reusable component patterns
- Configuration-driven environments
- Accessibility checks with axe-core-compatible browser injection hooks
- UX checks across multiple viewports
- Failure evidence: screenshots and traces
- Structured test metadata and markers
- GitHub Actions quality gates
- Portfolio-oriented architecture and test strategy documentation

## Engineering Principles

1. Configuration over hard-coded environment logic.
2. Deterministic synthetic test data.
3. Fast smoke feedback before deeper regression.
4. Evidence captured on failure.
5. Clear separation between test intent and UI mechanics.
6. CI must run the same commands developers run locally.
7. No claim of quality without executable evidence.

## Project Structure

```text
framework/
  config.py
  pages/
  reporting/

tests/
  smoke/
  e2e/
  accessibility/
  ux/

config/
  demo.yaml

docs/
  ARCHITECTURE.md
  TEST_STRATEGY.md
  PORTFOLIO_CASE_STUDY.md

.github/workflows/
  quality-gate.yml
```

## Quick Start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium
pytest
```

## Demo Target

By default the framework uses `https://example.com`, a public synthetic target. Replace it only with environments you are authorized to test.

## Portfolio Context

This repository is a clean reference implementation derived from recurring architecture patterns used in larger private Quality Engineering projects. It is **not a copy of any private repository** and contains no private Git history, production hostnames, credentials, customer names or proprietary test data.

## Engineering Principle

> Build fast. Verify independently. Release with evidence.
