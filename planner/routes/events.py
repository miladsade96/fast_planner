"""
    This file will handle routing operations such as creating, updating, and deleting events.
"""

from fastapi import APIRouter, HTTPException, Body
from planner.models.events import Event
from typing import List
