"""
    Test Signup and signin routes
    Author: Milad Sadeghi.DM - EverLookNeverSee@GitHub
"""

import httpx
import pytest


@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@test.com",
        "password": "testpassword",
        "events": []
    }
    headers = {
        "accept": "application/json",
        "Content-type": "application/json"
    }
    test_response = {
        "message": "User created successfully"
    }
    response = await default_client.post("/user/signup", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response
