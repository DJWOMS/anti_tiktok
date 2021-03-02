import ormar

from fastapi_users.db import OrmarBaseUserModel, OrmarUserDatabase

from db import MainMata
from user.schemas import UserDB


class User(OrmarBaseUserModel):
    class Meta(MainMata):
        pass

    username: str = ormar.String(max_length=100, unique=True)


user_db = OrmarUserDatabase(UserDB, User)
