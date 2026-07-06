from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes.health import router as health_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging(settings.logging_level)

app = FastAPI(
    title="Atlas AI Recruiter",
    version="0.1.0",
    description="Production-ready backend foundation for Atlas AI",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(health_router, prefix="/api/v1")


@app.get("/")
def read_root() -> JSONResponse:
    return JSONResponse(
        {
            "name": "Atlas AI Recruiter",
            "version": "0.1.0",
            "status": "ok",
        }
    )
