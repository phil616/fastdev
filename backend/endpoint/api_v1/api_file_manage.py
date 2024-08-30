from response.std import URFRouter
from model.File import File
file_urf_router = URFRouter(prefix="/fileManage")


@file_urf_router.get("/list")
async def file_manage_list():
    files = await File.all()
    return files
