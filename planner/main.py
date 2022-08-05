"""
    This file is the main file of the planner.
"""

import uvicorn
from fastapi import FastAPI
from database.connection import conn
from planner.routes.users import user_router
from planner.routes.events import events_router
from fastapi.responses import RedirectResponse


app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(events_router, prefix="/event")


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
