from starlette.requests import Request

from user.schemas import UserDB


def send_sms_code(user: UserDB, request: Request) -> None:
    print(f"User {user.id} has registered. {123456}")


def after_verification(user: UserDB, request: Request) -> None:
    print(f"{user}")


def after_verification_request(user: UserDB, token: str, request: Request) -> None:
    print(f"{user} - {token}")
