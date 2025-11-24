"""Notion relay placeholder for Run-Ledger and Registry sync."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NotionPayload:
    database_id: str
    properties: dict


def send(payload: NotionPayload) -> None:
    print(f"NOTION:::{payload.database_id}::{payload.properties}")

