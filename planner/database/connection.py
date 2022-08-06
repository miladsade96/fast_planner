"""
    This file will handle the database abstractions and configurations.
"""

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings
from planner.models.users import User
from planner.models.events import Event


class Settings(BaseSettings):
    """
        This class will handle the configurations for the database.
    """
    DATA_BASE_URL: Optional[str] = None

    async def initialize_database(self):
        """
            This method will initialize the database.
        """
        client = AsyncIOMotorClient(self.DATA_BASE_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event, User])

        class Config:
            env_file = '.env'
