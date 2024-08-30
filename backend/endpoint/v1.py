from fastapi import APIRouter
from endpoint.api_v1.api_authorize import authorize_router
from endpoint.api_v1.api_user import user_router
from endpoint.api_v1.api_cache import cache_router
from endpoint.api_v1.api_file import file_router
from endpoint.api_v1.api_file_manage import file_urf_router
from endpoint.api_v1.api_user_manage import user_manage_router
v1_router = APIRouter()

v1_router.include_router(authorize_router, prefix="/authorize", tags=["authorize"])
v1_router.include_router(user_router, prefix="/user", tags=["user"])
v1_router.include_router(cache_router, prefix="/cache", tags=["cache"])
v1_router.include_router(file_router, prefix="/file", tags=["file"])
v1_router.include_router(file_urf_router, prefix="/file_urf", tags=["file_urf"])
v1_router.include_router(user_manage_router, prefix="/user_manage", tags=["user_manage"])