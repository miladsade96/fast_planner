"""
    This file will be responsible for creating an instance of our application required by the test files.
    Author: Milad Sadeghi DM - EverLookNeverSee@GitHub
"""

import httpx
import pytest
import asyncio
from planner.main import app
from planner.models.users import User
from planner.models.events import Event
from planner.database.connection import Settings
