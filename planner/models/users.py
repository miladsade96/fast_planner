"""
    This file will contain the model definition for user operations.
"""

from pydantic import BaseModel, EmailStr


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
