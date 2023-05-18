#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import uvicorn

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from verbose_sniffle_py.api.v1 import router as v1_router
from verbose_sniffle_py.dependencies import dependencies
from verbose_sniffle_py.settings import SETTINGS


middleware = Middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE"],
    allow_headers=["*"],
)

app = FastAPI(
    title="verbose-sniffle-py",
    description="verbose-sniffle-py fastapi example",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    dependencies=dependencies,
    middleware=[middleware],
)

app.include_router(v1_router)

uvicorn.run(
    app=app,
    host=SETTINGS.APP_HOST,
    port=SETTINGS.APP_PORT,
)
