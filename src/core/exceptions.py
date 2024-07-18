from fastapi import Request
from schema.response import GSResp
async def global_exception_handler(_: Request, exc: Exception):
    # 捕获所有异常
    error_message = str(exc)
    # 根据需要进行错误信息的处理和格式化
    error_response = {
        "error": "An unexpected error occurred.",
        "detail": error_message
    }
    # 返回JSON格式的错误响应
    return GSResp(data=error_response, code=exc,message="ERROR")

async def database_exception_handler(_: Request, exc: Exception):
    ...

async def validation_exception_handler(_: Request, exc: Exception):
    ...
