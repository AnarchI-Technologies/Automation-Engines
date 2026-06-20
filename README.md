# Automation Engines

Reusable deterministic engines for AnarchI Technologies workflows.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Automation Engines collects the low-level machinery that turns events into actions. The design target is controlled execution: predictable inputs, explicit routing, and reviewable outputs.

## Current Components

```text
Automation Engines/
├── event_bridge_core.py
└── ui_coordinates_map.json
```

## Scope

- Event bridges and routing logic.
- Operator interface coordinate maps.
- Deterministic action sequencing.
- Guarded handoff points for external systems.

## Production Notes

- Validate event schemas before execution.
- Keep UI automation maps documented and versioned.
- Add dry-run modes before write-capable actions.
- Never commit secrets, browser profiles, or live account state.