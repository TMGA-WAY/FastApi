from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
from db.databse import get_db
from fastapi import Depends, HTTPException, status
from db import db_user

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '687b0e9adcbc5adac4c0831dd69f72630495b69634a2a18b6320682326c2a9aa'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_schema),
                     db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name: str = payload.get("sub")
        if user_name is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    user = db_user.get_user_by_username(db, user_name)
    if user is None:
        raise credential_exception
    return user
