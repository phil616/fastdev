from endpoint.v1 import v1_router
from endpoint.v2 import v2_router

from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

api_router.include_router(v1_router)
api_router.include_router(v2_router)

