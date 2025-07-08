# app/services/task_service.py
from typing import List
from ..models import Task
from datetime import datetime, timezone
import uuid
from ..interfaces import ITaskService

class TaskService(ITaskService):
    tasks = []
    def create_task(self, deal_id: str, description: str) -> Task:
        task = Task(
            id=str(uuid.uuid4()), deal_id=deal_id,
            description=description, created_at=datetime.now(timezone.utc))
        TaskService.tasks.append(task)
        return task

    def list_tasks(self, deal_id: str) -> List[Task]:
        return [t for t in TaskService.tasks if t.deal_id == deal_id]
