from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class Trigger:
    source: str
    action: str
    security_tier: int
    payload: dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class EventDecision:
    event_id: str
    route: str
    reason: str
    dry_run: bool
    timestamp: str


class EventBridge:
    """Deterministic event bridge for controlled automation handoffs."""

    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run

    def route(self, trigger: Trigger) -> EventDecision:
        event_id = f"evt_{uuid4().hex[:12]}"
        timestamp = datetime.now(timezone.utc).isoformat()

        if not trigger.source.strip():
            return self._decision(event_id, "reject", "source is required", timestamp)

        if trigger.security_tier < 0 or trigger.security_tier > 5:
            return self._decision(event_id, "reject", "security_tier must be between 0 and 5", timestamp)

        action = trigger.action.strip().upper()
        if action in {"WRITE", "TRANSFER", "DEPLOY", "DELETE"} and trigger.security_tier < 4:
            return self._decision(event_id, "hold", "write-capable action requires tier 4 clearance", timestamp)

        if action in {"OBSERVE", "REPORT", "SYNC"}:
            return self._decision(event_id, "execute", "read-safe automation route approved", timestamp)

        if action in {"WRITE", "TRANSFER", "DEPLOY", "DELETE"}:
            return self._decision(event_id, "review", "write-capable route requires operator review", timestamp)

        return self._decision(event_id, "review", "unrecognized action requires review", timestamp)

    def _decision(self, event_id: str, route: str, reason: str, timestamp: str) -> EventDecision:
        return EventDecision(
            event_id=event_id,
            route=route,
            reason=reason,
            dry_run=self.dry_run,
            timestamp=timestamp,
        )

