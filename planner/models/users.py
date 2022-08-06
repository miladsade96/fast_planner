"""
    This file will contain the model definition for user operations.
"""

from typing import List, Optional
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from planner.models.events import Event



class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "name@host.com",
                "password": "strong!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    schema_extra = {
        "example": {
            "email": "name@host.com",
            "password": "strong!!!"
        }
    }
