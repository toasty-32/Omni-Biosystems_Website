from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class UserProfile(BaseModel):
    uid: str
    email: str
    display_name: str | None = None
    role: Literal['admin', 'researcher', 'viewer'] = 'viewer'
    organization: str | None = None
    created_at: datetime


class UserProfileUpdate(BaseModel):
    display_name: str | None = None
    organization: str | None = None
