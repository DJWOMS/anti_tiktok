from typing import List

from pydantic import BaseModel

from user.schemas import UserOut


class FollowerCreate(BaseModel):
    username: str


class FollowerList(BaseModel):
    user: UserOut
    subscriber: UserOut
