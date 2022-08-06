"""
    This file will handle routing operations such as the registration and signing-in of users.
"""

from fastapi import APIRouter, HTTPException, status
from planner.models.users import User, UserSignIn
from planner.database.connection import Database
from planner.models.users import UserSignIn, User

# Defining a router for the users endpoint
user_router = APIRouter(tags=["User"])

user_database = Database(User)


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await user.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    else:
        await user_database.save(user)
        return {"message": "User created successfully"}


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "User signed in successfully"
    }
