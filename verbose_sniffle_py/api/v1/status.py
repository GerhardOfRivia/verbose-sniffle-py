#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from fastapi import APIRouter

from verbose_sniffle_py.models.v1.status import SystemStatus, StatusResponse

router = APIRouter()


@router.get("/status", tags=["system"])
async def status() -> StatusResponse:
    return StatusResponse(status=SystemStatus.PASS)
