from fastapi import APIRouter
from .endpoints import users, samples, analysis, dashboard

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(samples.router)
api_router.include_router(analysis.router)
api_router.include_router(dashboard.router)
