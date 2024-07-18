from fastapi import APIRouter,FastAPI,Request
from fastapi.openapi.docs import (get_redoc_html, get_swagger_ui_html)
from fastapi.openapi.utils import get_openapi
from config import settings
openapi_router = APIRouter()



# custom_openapi
def custom_openapi(application:FastAPI):
    if application.openapi_schema:
        return application.openapi_schema
    openapi_schema = get_openapi(
        description=settings.APP_DESC,
        version=settings.APP_VERSION,
        title=settings.APP_NAME,
        routes=application.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": settings.LOGO_URL
    }
    application.openapi_schema = openapi_schema
    return application.openapi_schema


# custom_swagger_ui_html
@openapi_router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request:Request):
    return get_swagger_ui_html(
        openapi_url=request.app.openapi_url,
        title=request.app.title + " - Swagger UI",
        oauth2_redirect_url=request.app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/swagger-ui-bundle.js",
        swagger_css_url="/swagger-ui.css",
    )


@openapi_router.get("/redoc", include_in_schema=False)
async def redoc_html(request:Request):
    return get_redoc_html(
        openapi_url=request.app.openapi_url,
        title=request.app.title + " - ReDoc",
        redoc_js_url="/redoc.standalone.js",
    )
