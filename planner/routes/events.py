"""
    This file will handle routing operations such as creating, updating, and deleting events.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from planner.models.events import Event, EventUpdate
from planner.database.connection import get_session
from sqlmodel import select
from typing import List


# Defining event router
events_router = APIRouter(tags=["Events"])


@events_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    """
        This function will retrieve all events.
    """
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@events_router.get("/{event_id}", response_model=Event)
async def retrieve_event(event_id: int, session=Depends(get_session)) -> Event:
    """
        This function will retrieve an event by id.
    """
    event = session.get(Event, event_id)
    if event:
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied id does not exist.")


@events_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message": "Event created successfully"}


@events_router.put("/edit/{event_id}", response_model=Event)
async def update_event(event_id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, event_id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied id does not exist.")


@events_router.delete("/{event_id}")
async def delete_event(event_id: int, session=Depends(get_session)) -> dict:
    """
        This function will delete an event by id.
    """
    event = session.get(Event, event_id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event with supplied id does not exist.")


@events_router.delete("/")
async def delete_all_events(session=Depends(get_session)) -> dict:
    """
    This function will delete all events.
    """
    session.query(Event).delete()
    session.commit()
    return {"message": "All events deleted successfully"}
