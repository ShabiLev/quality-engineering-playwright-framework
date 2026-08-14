# Architecture

## Layers

```text
Configuration
   ↓
Fixtures
   ↓
Page Objects / Components
   ↓
Test Intent
   ↓
Evidence + CI
```

The architecture separates environment configuration from UI mechanics and test intent. Tests should describe behavior; page objects encapsulate selectors and interaction details.

## Why this structure

- Reuse UI mechanics without hiding test intent.
- Swap authorized targets through configuration rather than code edits.
- Keep smoke, E2E, accessibility and UX suites independently selectable.
- Make failures diagnosable through Playwright evidence.

## Security Boundary

No credentials are committed. Environment overrides use `QE_BASE_URL`; authenticated examples should use CI secrets or local environment variables rather than repository files.
