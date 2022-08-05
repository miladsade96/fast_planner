"""
    This file will contain the model definition for events operations.
"""

from typing import List, Optional
from sqlmodel import SQLModel, Field, Column, JSON


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "Event Title",
                "image": "https://image.com/image.png",
                "description": "Event Description",
                "tags": ["tag1", "tag2"],
                "location": "Event Location"
            }
        }
