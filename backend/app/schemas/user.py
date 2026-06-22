from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal


class UserProfile(BaseModel):
    id: str
    email: EmailStr
    full_name: str | None = None
    role: Literal['admin', 'researcher', 'viewer'] = 'viewer'
    organization: str | None = None
    created_at: datetime


class UserProfileUpdate(BaseModel):
    full_name: str | None = None
    organization: str | None = None
