"""
    This module handles the authentication of the user.
    Author: Milad Sadeghi DM - EverLookNeverSee@GitHub
"""

from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from planner.auth.jwt_handler import verify_access_token
