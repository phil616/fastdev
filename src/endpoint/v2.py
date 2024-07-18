from fastapi import APIRouter
from schema.response import GSResp
from fastapi import HTTPException
v2_router = APIRouter(prefix="/v2")


@v2_router.get("/")
async def api_v1_router_get():
    raise HTTPException(status_code=403, detail="API V2")
    return GSResp({"message":"API V2"})