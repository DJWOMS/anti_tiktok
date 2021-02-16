from typing import IO, Generator

import filetype
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, BackgroundTasks
from starlette.requests import Request
from starlette.responses import StreamingResponse
from starlette.templating import Jinja2Templates

from schemas import UploadVideo, GetVideo, Message
from models import Video, User
from services import save_video

video_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@video_router.post("/")
async def create_video(
        back_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
):
    user = await User.objects.first()
    return await save_video(user, file, title, description, back_tasks)


@video_router.get("/video/{video_pk}", responses={404: {"model": Message}})
def get_video(video_pk: int):
    file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open(file.file, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")



