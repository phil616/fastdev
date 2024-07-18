from fastapi import FastAPI,HTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from endpoint import api
from core.proxy import bind_context_request
from core.lifespan import app_lifespan
from core.middlewares import BaseMiddleware
from config import settings
from core.exceptions import global_exception_handler
app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=app_lifespan,
    # openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set all CORS enabled origins
if settings.ENABLE_BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )

# static files
staticfile = StaticFiles(directory="static")
app.mount("/static", staticfile, name="static")

# app.mount('/', StaticFiles(directory=settings.STATIC_DIR), name="static")
# app.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)

# api router
app.include_router(api.api_router)
# lifespan setup and shutdowns

# context vars
app.middleware("http")(bind_context_request)
# HTTP middlewares
app.middleware(BaseMiddleware)
# Exception handlers
app.add_exception_handler(HTTPException,global_exception_handler)

