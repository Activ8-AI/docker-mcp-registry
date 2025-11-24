"""Telemetry engine stub capturing heartbeat and drift signals."""
from __future__ import annotations

import random
import time
from typing import Dict

DRIFT_THRESHOLDS = {"green": (0, 10), "yellow": (11, 30), "red": (31, 100)}


def classify_drift(score: int) -> str:
    for label, (low, high) in DRIFT_THRESHOLDS.items():
        if low <= score <= high:
            return label
    return "unknown"


def emit(signal: Dict[str, str]) -> None:
    print(f"TELEMETRY::{signal}")


def heartbeat() -> None:
    score = random.randint(0, 100)
    state = classify_drift(score)
    emit({"heartbeat": "1", "drift": str(score), "state": state})


if __name__ == "__main__":
    while True:
        heartbeat()
        if classify_drift(random.randint(0, 100)) == "red":
            print("SRR invoked; pausing loop")
            break
        time.sleep(5)
