# app/main.py
from fastapi import FastAPI, Depends
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from contextlib import asynccontextmanager

from .facades.deal_facade import DealFacade
from .dependencies import get_deal_facade, get_deal_coordinator, get_task_service

scheduler = AsyncIOScheduler()

def _create_facade() -> DealFacade:
    task_srv = get_task_service()
    coordinator = get_deal_coordinator()
    return DealFacade(coordinator=coordinator, task_service=task_srv)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: schedule and start the pipeline job
    facade = _create_facade()
    scheduler.add_job(facade.run_pipeline, IntervalTrigger(minutes=60), id="deal_sync_job")
    scheduler.start()

    yield  # Application is running...

    # Shutdown: gracefully stop the scheduler
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

@app.post("/run")
def run_manual(facade: DealFacade = Depends(get_deal_facade)):
    print("inside run manual")
    facade.run_pipeline()
    return {"status": "ok"}

@app.get("/deals/{deal_id}/tasks")
def get_tasks(deal_id: str, facade: DealFacade = Depends(get_deal_facade)):
    return facade.get_tasks(deal_id)
