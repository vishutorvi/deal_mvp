# app/dependencies.py
from typing import Annotated
from fastapi import Depends
from .services.task_service import TaskService
from .agents.coordinator import DealCoordinator
from .facades.deal_facade import DealFacade

def get_task_service() -> TaskService:
    return TaskService()

def get_deal_coordinator() -> DealCoordinator:
    return DealCoordinator()

def get_deal_facade(
    coordinator: Annotated[DealCoordinator, Depends(get_deal_coordinator)],
    task_srv: Annotated[TaskService, Depends(get_task_service)],
) -> DealFacade:
    return DealFacade(coordinator, task_srv)
