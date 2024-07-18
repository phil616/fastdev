from fastapi import APIRouter
from schema.response import GSResp
v1_router = APIRouter(prefix="/v1")


@v1_router.get("/")
async def api_v1_router_get():
    return GSResp({"message":"API V1"})