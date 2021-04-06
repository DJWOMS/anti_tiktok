from pydantic import BaseModel

from user.schemas import User


class UploadVideo(BaseModel):
    title: str
    description: str


class GetListVideo(BaseModel):
    id: int
    title: str
    description: str
    like_count: int


class GetVideo(GetListVideo):
    user: User


class Message(BaseModel):
    message: str
