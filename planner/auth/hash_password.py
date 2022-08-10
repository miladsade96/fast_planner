"""
    This module is used to hash a password.
    Author: Milad sadeghi DM - EverLookNeverSee@GitHub
"""

from passlib.context import CryptContext

# Password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
