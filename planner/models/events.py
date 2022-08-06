"""
    This file will contain the model definition for events operations.
"""

from beanie import Document
from typing import List, Optional


class Event(Document):
    """
    This class will contain the model definition for events operations.
    """
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Event Title",
                "image": "https://image.com/image.jpg",
                "description": "Event Description",
                "tags": ["tag1", "tag2"],
                "location": "Event Location"
            }
        }

    class Settings:
        name = "events"
