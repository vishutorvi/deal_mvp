# app/models.py
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Deal(BaseModel):
    id: str
    stage: str
    last_updated: datetime
    close_date: Optional[datetime]

class Task(BaseModel):
    id: str
    deal_id: str
    description: str
    created_at: datetime
