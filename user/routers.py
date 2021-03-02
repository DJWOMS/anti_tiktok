from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from user.api import on_after_register
from user.models import user_db
from user.schemas import User, UserDB, UserCreate, UserUpdate
from user.auth import auth_backends, jwt_authentication


user_router = APIRouter()


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
# user_router.include_router(
#     fastapi_users.get_reset_password_router(
#         SECRET, after_forgot_password=on_after_forgot_password
#     ),
#     prefix="/auth",
#     tags=["auth"],
# )
# user_router.include_router(
#     fastapi_users.get_verify_router(
#         SECRET, after_verification_request=after_verification_request
#     ),
#     prefix="/auth",
#     tags=["auth"],
# )
user_router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
