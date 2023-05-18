#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from fastapi import APIRouter

from .status import router as status_router

router = APIRouter(prefix="/v1")
router.include_router(status_router)
