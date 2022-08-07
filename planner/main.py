"""
    This file is the main file of the planner.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import Settings
from planner.routes.events import events_router
from planner.routes.users import user_router


app = FastAPI()

settings = Settings()

# Register routes
app.include_router(user_router, prefix="/user")
app.include_router(events_router, prefix="/event")


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
