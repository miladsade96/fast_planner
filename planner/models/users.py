"""
    This file will contain the model definition for user operations.
"""

from typing import List, Optional
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from planner.models.events import Event



class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = 'users'

    class Config:
        schema_extra = {
            "example": {
                "email": "name@host.com",
                "password": "strong!!!",
                "events": [],
            }
        }


# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "name@host.com",
#                 "password": "strong!!!"
#             }
#         }

    class Config:
        schema_extra = {
            "example": {
                "email": "name@host.com",
                "password": "strong!!!"
            }
        }
