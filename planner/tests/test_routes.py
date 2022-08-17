"""
    This module contains the tests for the routes module.
    Author: Milad Sadeghi DM - EverLookNeverSee@Github
"""

import httpx
import pytest
from planner.models.events import Event
from planner.auth.jwt_handler import create_access_token
