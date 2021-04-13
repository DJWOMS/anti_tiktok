import jwt
from datetime import datetime, timedelta


ALGORITHM = "HS256"
access_token_jwt_subject = "access"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = "Sdasdad3w#RmF34ef43%E5&*6DV%$5DSvBF*fY9V(y*&VNFdfBU(t8DnfDS"


def create_token(user_id: int) -> dict:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expires
        ),
        "token_type": "Token",
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Создание токена"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
