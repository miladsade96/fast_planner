"""
    This file will contain the model definition for user operations.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from planner.models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "your_email@test.com",
                "username": "your_username",
                "events": [],
            }
        }
