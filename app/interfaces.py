# app/interfaces.py
from typing import List
from .models import Task

class IDealCoordinator():
    def run(self) -> None: ...

class ITaskService():
    def list_tasks(self, deal_id: str) -> List[Task]: ...
