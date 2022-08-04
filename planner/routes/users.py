"""
    This file will handle routing operations such as the registration and signing-in of users.
"""

from fastapi import APIRouter, HTTPException, status
from planner.models.users import User, UserSignIn

# Defining a router for the users endpoint
users_router = APIRouter(tags=["User"])

# Create users
users = {}
