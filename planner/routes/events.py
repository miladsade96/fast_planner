"""
    This file will handle routing operations such as creating, updating, and deleting events.
"""

from fastapi import APIRouter, HTTPException, Depends, Request, status
from planner.models.events import Event, EventUpdate
from planner.database.connection import get_session
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
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message": "Event created successfully"}


@events_router.delete("/{event_id}")
async def delete_event(event_id: int) -> dict:
    """
        This function will delete an event by id.
    """
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=404, detail="Event not found")


@events_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "All events deleted successfully"}
