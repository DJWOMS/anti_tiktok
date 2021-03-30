from typing import Optional, Union, Dict

import ormar
from db import MainMata

from user.models import User


class Follower(ormar.Model):
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True)
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="user")
    subscriber: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="subscriber")
