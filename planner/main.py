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

app.include_router(user_router, prefix="/user")
app.include_router(events_router, prefix="/event")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
