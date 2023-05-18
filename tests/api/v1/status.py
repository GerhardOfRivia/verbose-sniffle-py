#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import pytest
from httpx import AsyncClient

from verbose_sniffle_py.app import app


@pytest.mark.anyio
async def test_status():
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as ac:
        response = await ac.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "PASS"}
