"""
    This file will handle routing operations such as creating, updating, and deleting events.
"""
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status, Depends
from planner.database.connection import Database
from planner.models.events import Event, EventUpdate
from typing import List
from planner.auth.authenticate import authenticate



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
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    await event_database.save(body)
    return {"message": "Event created successfully"}


@events_router.put("/{event_id}", response_model=Event)
async def update_event(event_id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    """
        This function will update an event.
    """
    event = await event_database.get(event_id)
    if event.creator != user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You do not have permission to update this event")
    updated_event = await event_database.update(event_id, body)
    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event with supplied ID does not exist")
    return updated_event


@events_router.delete("/{event_id}")
async def delete_event(event_id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    """
        This function will delete an event by id.
    """
    event = await event_database.get(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    elif event.creator != user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You do not have permission to delete this event")
    else:
        await event_database.delete(event_id)
        return {"message": "Event deleted successfully"}
