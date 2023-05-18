#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import enum
from pydantic import BaseModel


class SystemStatus(enum.StrEnum):
    PASS = enum.auto()
    FAIL = enum.auto()


class StatusResponse(BaseModel):
    status: SystemStatus = SystemStatus.PASS
