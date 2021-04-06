import datetime
import ormar
from typing import Optional, Union, Dict, List
from db import MainMata

from user.models import User


class UserLike(ormar.Model):
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True)


class Video(ormar.Model):
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=50)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="user_video")
    like_count: int = ormar.Integer(default=0)
    like_user: Optional[Union[List[User], Dict]] = ormar.ManyToMany(
        User, related_name="like_users", through=UserLike
    )


# , through=UserLike
