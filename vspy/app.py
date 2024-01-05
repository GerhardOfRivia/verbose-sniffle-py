import uvicorn

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from vspy.api.v1 import router as v1_router
from vspy.core.logging import setup_logging
from vspy.settings import SETTINGS

setup_logging()

middleware = Middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE"],
    allow_headers=["*"],
)

app = FastAPI(
    title="verbose-sniffle-py",
    description="fastapi sqlite project",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    middleware=[middleware],
)

app.include_router(v1_router)

uvicorn.run(
    app=app, host=SETTINGS.APP_HOST, port=SETTINGS.APP_PORT,
)
