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


@events_router.get("/")
async def retrieve_all_events() -> List[Event]:
    """
        This function will retrieve all events.
    """
    return events


@events_router.get("/{event_id}")
async def retrieve_event(event_id: int) -> Event:
    """
        This function will retrieve an event by id.
    """
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")


@events_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {"message": "Event created successfully"}
