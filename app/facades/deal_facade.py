# app/facades/deal_facade.py
from ..interfaces import IDealCoordinator, ITaskService

class DealFacade:
    def __init__(self, coordinator: IDealCoordinator, task_service: ITaskService):
        self._coord = coordinator
        self._task_srv = task_service

    def run_pipeline(self):
        self._coord.run()

    def get_tasks(self, deal_id: str):
        return self._task_srv.list_tasks(deal_id)
