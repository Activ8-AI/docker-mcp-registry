"""Teamwork sink stub for task creation and updates."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    name: str
    description: str
    status: str = "pending"


def create_task(task: Task) -> None:
    print(f"TEAMWORK::CREATE::{task.name}::{task.status}")

