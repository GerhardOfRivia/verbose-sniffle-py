#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8

import enum
from pydantic import BaseSettings


class Environment(enum.StrEnum):
    PROD = enum.auto()
    TEST = enum.auto()


class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True
    ENV: Environment = Environment.TEST
    MAX_PAGE_SIZE: int = 100


SETTINGS = Settings()
