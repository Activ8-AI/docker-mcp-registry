"""MAOS MCP Relay Server stub implementing charter guardrails and telemetry hooks."""
from __future__ import annotations

import json
import logging
import pathlib
import time
from dataclasses import dataclass
from typing import Any, Dict, Iterable

CONFIG_PATH = pathlib.Path(__file__).resolve().parents[2] / "configs" / "global_config.yaml"
LOGGER = logging.getLogger("maos.mcp.relay")


def load_config() -> Dict[str, Any]:
    """Lazy loader for the global config; keeps file-based artifact simple."""
    try:
        import yaml  # type: ignore
    except ImportError as exc:  # pragma: no cover - runtime guard
        raise RuntimeError("PyYAML is required to boot the MCP relay server") from exc

    with CONFIG_PATH.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


@dataclass
class RelayEnvelope:
    """Transport-neutral payload for MCP requests."""

    task_id: str
    actor: str
    payload: Dict[str, Any]
    timestamp: float
    seal_version: str

    def serialize(self) -> str:
        return json.dumps(
            {
                "task_id": self.task_id,
                "actor": self.actor,
                "payload": self.payload,
                "timestamp": self.timestamp,
                "seal_version": self.seal_version,
            },
            sort_keys=True,
        )


class CharterGuard:
    """Applies STOP–RESET–REALIGN enforcement before relaying commands."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def validate(self, envelope: RelayEnvelope) -> None:
        if envelope.actor not in {"prime", "claude", "agent"}:
            raise PermissionError("Actor is not registered under the Charter")
        if envelope.payload.get("drift", 0) > 30:
            raise RuntimeError("Charter drift exceeds yellow threshold; SRR invoked")


class MCPRelayServer:
    """Reference implementation for board review and future automation."""

    def __init__(self, charter_guard: CharterGuard):
        self.guard = charter_guard

    def relay(self, envelopes: Iterable[RelayEnvelope]) -> None:
        for envelope in envelopes:
            self.guard.validate(envelope)
            LOGGER.info("relay.accepted", extra={"task_id": envelope.task_id})
            self.emit_telemetry(envelope)

    @staticmethod
    def emit_telemetry(envelope: RelayEnvelope) -> None:
        LOGGER.debug("telemetry", extra={"serialized": envelope.serialize()})


if __name__ == "__main__":  # pragma: no cover - manual activation path
    logging.basicConfig(level=logging.INFO)
    config = load_config()
    server = MCPRelayServer(CharterGuard(config))
    sample = RelayEnvelope(
        task_id="TEST-000",
        actor="prime",
        payload={"heartbeat": True},
        timestamp=time.time(),
        seal_version="MVP_v0",
    )
    server.relay([sample])
