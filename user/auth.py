import jwt
from jwt import PyJWTError
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN

from .models import User

from .tokenizator import ALGORITHM, SECRET_KEY
from .schemas import TokenPayload


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


async def get_current_user(token: str = Security(reusable_oauth2)):
    """ Check auth user
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = await User.objects.get_or_none(id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_user(current_user: User = Security(get_current_user)):
    """ Проверка активный юзер или нет """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_superuser(current_user: User = Security(get_current_user)):
    """ Проверка суперюзер или нет """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
