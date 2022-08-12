"""
    This file will handle routing operations such as the registration and signing-in of users.
"""

from fastapi import APIRouter, HTTPException, status, Depends
from planner.database.connection import Database
from planner.models.users import User, TokenResponse
from planner.auth.hash_password import HashPassword
from fastapi.security import OAuth2PasswordRequestForm
from planner.auth.jwt_handler import create_access_token


# Defining a router for the users endpoint
user_router = APIRouter(tags=["User"])

user_database = Database(User)

hash_password = HashPassword()


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await user.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    else:
        hashed_password = hash_password.create_hash(user.password)
        user.password = hashed_password
        await user_database.save(user)
        return {"message": "User created successfully"}


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.username)
    if user_exist:
        if hash_password.verify_hash(user.password, user_exist.password):
            access_token = create_access_token(user_exist.email)
            return {"access_token": access_token, "token_type": "Bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
