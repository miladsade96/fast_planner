"""
    This file will handle the database abstractions and configurations.
"""

from planner.models.events import Event
from sqlmodel import SQLModel, Session, create_engine
