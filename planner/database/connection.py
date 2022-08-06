"""
    This file will handle the database abstractions and configurations.
"""

from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Any, List
from pydantic import BaseSettings, BaseModel
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


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        """
            This method will save the document to the database.
        """
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        """
            This method will get the document from the database.
        """
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        """
            This method will get all the documents from the database.
        """
        docs = await self.model.find_all().to_list()
        if docs:
            return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        """
            This method will update the document in the database.
        """
        doc_id = id
        des_body = body.dict()
        des_body = {k:v for k, v in des_body.items() if v is not None}
        update_query = {'$set':{
            field: value for field, value in des_body.items()
        }}
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        """
            This method will delete the document from the database.
        """
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

    async def delete_all(self) -> bool:
        """
            This method will delete all the documents from the database.
        """
        docs = await self.get_all()
        if not docs:
            return False
        for doc in docs:
            await doc.delete()
        return True
