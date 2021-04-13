from pydantic import BaseModel

from user.schemas import UserOut


class UploadVideo(BaseModel):
    title: str
    description: str


class GetListVideo(BaseModel):
    id: int
    title: str
    description: str
    like_count: int


class GetVideo(GetListVideo):
    user: UserOut


class Message(BaseModel):
    message: str
