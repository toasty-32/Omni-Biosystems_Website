from pydantic import BaseModel
from datetime import datetime


class AnalysisResult(BaseModel):
    id: str
    sample_id: str
    result_type: str
    value: float
    unit: str
    reference_range: str | None = None
    flagged: bool
    created_at: datetime


class AnalysisResultCreate(BaseModel):
    sample_id: str
    result_type: str
    value: float
    unit: str
    reference_range: str | None = None
    flagged: bool = False


class DashboardStats(BaseModel):
    total_samples: int
    pending_samples: int
    completed_samples: int
    flagged_results: int
