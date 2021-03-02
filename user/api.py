from starlette.requests import Request

from user.schemas import UserDB


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")
