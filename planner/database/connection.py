"""
    This file will handle the database abstractions and configurations.
"""

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings
