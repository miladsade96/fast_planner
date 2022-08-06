"""
    This file will handle routing operations such as creating, updating, and deleting events.
"""
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from planner.database.connection import Database
from planner.models.events import Event, EventUpdate
from typing import List



# Defining event router
events_router = APIRouter(tags=["Events"])


event_database = Database(Event)


@events_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    """
        This function will retrieve all events.
    """
    events = await event_database.get_all()
    return events


@events_router.get("/{event_id}", response_model=Event)
async def retrieve_event(event_id: PydanticObjectId) -> Event:
    """
        This function will retrieve an event by id.
    """
    event = await event_database.get(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return event


@events_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {"message": "Event created successfully"}


@events_router.put("/{event_id}", response_model=Event)
async def update_event(event_id: PydanticObjectId, body: EventUpdate) -> Event:
    """
        This function will update an event.
    """
    updated_event = await event_database.update(event_id, body)
    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return updated_event


@events_router.delete("/{event_id}")
async def delete_event(event_id: PydanticObjectId) -> dict:
    """
        This function will delete an event by id.
    """
    event = await event_database.delete(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return {"message": "Event deleted successfully"}


@events_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "All events deleted successfully"}
