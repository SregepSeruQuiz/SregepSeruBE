from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncConnection
from jose import jwt

from api.depends.db import get_conn
from user.exceptions import IdNotFoundError
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")




