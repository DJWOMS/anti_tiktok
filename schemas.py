from typing import List

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    title: str
    description: str


class Message(BaseModel):
    message: str
