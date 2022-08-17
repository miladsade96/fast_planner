"""
    This module contains the tests for the routes module.
    Author: Milad Sadeghi DM - EverLookNeverSee@Github
"""

import httpx
import pytest
from planner.models.events import Event
from planner.auth.jwt_handler import create_access_token


@pytest.fixture(scope="module")
async def access_token():
    """
    This fixture is used to create an access token for the tests.
    :return: access token
    """
    return create_access_token("testuser@test.com")


@pytest.fixture(scope="module")
async def mock_event() -> Event:
    new_event = Event(
        creator="testuser@test.com",
        title="Mock Event",
        image="https://image.com/image.jpg",
        description="Mock Event Description",
        tags=["tag1", "tag2"],
        location="Mock Event Location"
    )
    await Event.insert_one(new_event)
    yield new_event


@pytest.mark.asyncio
async def test_get_events(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    response = await default_client.get("/event/")
    assert response.status_code == 200
    assert response.json()[0]["_id"] == str(mock_event.id)


@pytest.mark.asyncio
async def test_get_event(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.get(url)
    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["_id"] == str(mock_event.id)


@pytest.mark.asyncio
async def test_create_event(default_client: httpx.AsyncClient, access_token: str) -> None:
    payload = {
        "title": "New Event",
        "image": "https://image.com/image.jpg",
        "description": "New Event Description",
        "tags": ["new", "event"],
        "location": "New Event Location"
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    test_response = {"message": "Event created successfully"}
    response = await default_client.post("/event/new", headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_get_events_count(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    response = await default_client.get("/event/")
    events = response.json()
    assert response.status_code == 200
    assert len(events) == 2
