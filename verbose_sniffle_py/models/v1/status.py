#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import enum
from pydantic import BaseModel

from verbose_sniffle_py.core.enum import AutoEnum


class SystemStatus(AutoEnum):
    PASS = enum.auto()
    FAIL = enum.auto()


class StatusResponse(BaseModel):
    status: SystemStatus = SystemStatus.PASS
