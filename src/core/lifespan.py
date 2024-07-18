from fastapi import FastAPI
import contextlib
from core.logger import log

@contextlib.asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Email
    # Database 
    # LoadCache
    # Component Register
    # Run backgroud tasks

    log.info("Starting Up lifespan")
    yield
    log.info("Shutting Down lifespan")