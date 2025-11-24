"""Slack Signal Bot stub for standups and alerts."""
from __future__ import annotations


def post(channel: str, message: str) -> None:
    payload = {"channel": channel, "text": message}
    print(f"SLACK::{payload}")

