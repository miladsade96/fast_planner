"""
    This file will handle routing operations such as creating, updating, and deleting events.
"""

from fastapi import APIRouter, HTTPException, Body
from planner.models.events import Event
from typing import List


# Defining event router
events_router = APIRouter(tags=["Events"])

# Events list
events: List[Event] = []
