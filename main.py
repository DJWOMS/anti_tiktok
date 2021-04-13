from fastapi import FastAPI
from db import database, metadata, engine

from followers.api import follower_router
from video.api import video_router
from user.api import user_router


app = FastAPI()

metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(user_router)
app.include_router(video_router)
app.include_router(follower_router)

