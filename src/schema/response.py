from pydantic import BaseModel
from typing import Any,Union
from starlette.responses import JSONResponse
class SRFResponse(BaseModel):
    code: int = 0
    message: Union[str, None] = None
    data: Union[dict[str, Any] , None] = None

def GSResp(
        data: Union[dict[str, Any], None] = None,
        code: int=200,
        message: str='SUCCESS') -> SRFResponse:
    """
    Global Standard Response Format
    """
    return JSONResponse(SRFResponse(data=data, code=code, message=message).model_dump())