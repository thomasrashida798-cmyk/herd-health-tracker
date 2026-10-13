# Changelog

## 1.1.0 — Layered project structure

- Separated domain models, record services, console UI, input helpers, and validation utilities into dedicated modules.
- Split automated tests by functional area while retaining the original test cases.
- Added architecture, testing, and DPG-alignment documentation.
- Added package-based execution with `python -m herd_health_tracker_app` while preserving `python herd_health_tracker.py` as a simple launcher.
- Preserved the project's assignment scope, approved statuses, sample data, in-memory storage model, tuple summary, and console behaviour.
