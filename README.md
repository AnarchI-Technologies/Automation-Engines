# Automation Engines

Reusable deterministic event engines for AnarchI Technologies workflows.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Automation Engines turns structured triggers into controlled routes: execute, hold, review, or reject. It is designed for dry-run-first automation where write-capable work must pass explicit clearance and operator review.

## What Changed

- Removed gaming/payment-specific prototype language from the public repo.
- Rebuilt the event bridge as a small deterministic Python package.
- Moved UI coordinate data into a generic example config.
- Added tests for read-safe execution, write holds, write review, and invalid tiers.

## Structure

```text
.
|-- automation_engines/
|   |-- __init__.py
|   `-- event_bridge.py
|-- config/
|   `-- ui_coordinates_map.example.json
|-- tests/
|   `-- test_event_bridge.py
`-- README.md
```

## Verify

```bash
python -m unittest discover -s tests -q
```

## Public Safety

This repo should not contain live UI coordinates for private accounts, browser/session state, credentials, payment records, or irreversible write automation without dry-run and review gates.
