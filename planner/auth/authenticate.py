"""
    This module handles the authentication of the user.
    Author: Milad Sadeghi DM - EverLookNeverSee@GitHub
"""

from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from planner.auth.jwt_handler import verify_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    """
    This function authenticates the user.
    :param token: The token of the user.
    :return: The token of the user.
    """
    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Signin for access")
    decoded_token = verify_access_token(token)
    return decoded_token["user"]
