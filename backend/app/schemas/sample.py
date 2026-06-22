from pydantic import BaseModel
from datetime import datetime
from typing import Any, Literal


class SampleCreate(BaseModel):
    name: str
    type: str
    collected_at: datetime
    metadata: dict[str, Any] = {}


class SampleUpdate(BaseModel):
    name: str | None = None
    type: str | None = None
    status: Literal['pending', 'processing', 'completed', 'failed'] | None = None
    metadata: dict[str, Any] | None = None


class Sample(BaseModel):
    id: str
    name: str
    type: str
    status: Literal['pending', 'processing', 'completed', 'failed']
    collected_at: datetime
    processed_at: datetime | None = None
    owner_id: str
    metadata: dict[str, Any]
    created_at: datetime
