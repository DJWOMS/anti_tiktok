from typing import List

from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks, Depends
from starlette.requests import Request
from starlette.responses import StreamingResponse, HTMLResponse
from starlette.templating import Jinja2Templates

from user.auth import current_active_user

from .schemas import GetListVideo, GetVideo
from .models import Video, User
from .services import save_video, open_file

video_router = APIRouter(tags=["video"])
templates = Jinja2Templates(directory="templates")


@video_router.post("/")
async def create_video(
        back_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
        user: User = Depends(current_active_user)
):
    return await save_video(user, file, title, description, back_tasks)


# @video_router.get("/video/{video_pk}")
# async def get_video(video_pk: int):
#     file = await Video.objects.select_related('user').get(pk=video_pk)
#     file_like = open(file.file, mode="rb")
#     return StreamingResponse(file_like, media_type="video/mp4")


@video_router.get("/user/{user_name}", response_model=List[GetListVideo])
async def get_list_video(user_name: str):
    return await Video.objects.filter(user__username=user_name).all()


@video_router.get("/index/{video_pk}", response_class=HTMLResponse)
async def get_video(request: Request, video_pk: int):
    return templates.TemplateResponse("index.html", {"request": request, "path": video_pk})


@video_router.get("/video/{video_pk}")
async def get_streaming_video(request: Request, video_pk: int) -> StreamingResponse:
    file, status_code, content_length, headers = await open_file(request, video_pk)
    response = StreamingResponse(
        file,
        media_type='video/mp4',
        status_code=status_code,
    )

    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response


@video_router.get("/404", response_class=HTMLResponse)
async def error_404(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})


@video_router.post("/{video_pk}", status_code=201)
async def add_like(video_pk: int, user: User = Depends(current_active_user)):
    _video = await Video.objects.select_related("like_user").get(pk=video_pk)
    _user = await User.objects.get(id=user.id)
    if _user in _video.like_user:
        _video.like_count -= 1
        await _video.like_user.remove(_user)
    else:
        _video.like_count += 1
        await _video.like_user.add(_user)
    await _video.update()
    return _video.like_count



