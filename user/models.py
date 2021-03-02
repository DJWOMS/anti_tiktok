import ormar

from fastapi_users.db import OrmarBaseUserModel

from db import MainMata


class User(OrmarBaseUserModel):
    class Meta(MainMata):
        pass

    username: str = ormar.String(max_length=100, unique=True)
