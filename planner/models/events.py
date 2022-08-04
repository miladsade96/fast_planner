"""
    This file will contain the model definition for events operations.
"""

from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    """
    This class will contain the model definition for events operations.
    """
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Event Title",
                "image": "https://image.com/image.jpg",
                "description": "Event Description",
                "tags": ["tag1", "tag2"],
                "location": "Event Location"
            }
        }
