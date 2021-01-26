from fastapi import FastAPI
from api import video_router


app = FastAPI()


app.include_router(video_router)
