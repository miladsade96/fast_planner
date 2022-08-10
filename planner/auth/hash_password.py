"""
    This module is used to hash a password.
    Author: Milad sadeghi DM - EverLookNeverSee@GitHub
"""

from passlib.context import CryptContext

# Password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    """
        This class is used to hash a password and check if the password is correct.
    """
    @staticmethod
    def create_hash(password: str) -> str:
        """
        This method is used to hash a password
        :param password: password to be hashed
        :return: hashed password
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify_hash(plain_password: str, hashed_password: str) -> bool:
        """
        This method is used to verify if the password is correct
        :param plain_password: password to be verified
        :param hashed_password: hashed password
        :return: True if the password is correct, False otherwise
        """
        return pwd_context.verify(plain_password, hashed_password)
