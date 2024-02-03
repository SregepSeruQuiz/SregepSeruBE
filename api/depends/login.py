from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncConnection
from jose import jwt, JWTError
from user.facades.user import User

from api.depends.db import get_conn
from api.config import cfg
from user.exceptions import IdNotFoundError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_uuid(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, cfg.secret)
    except JWTError as e:
        raise HTTPException(403, {"error": str(e)})
    yield data['uuid']


async def get_user_id(conn: AsyncConnection = Depends(get_conn), uuid: str = Depends(get_uuid)):
    u = User(conn)
    try:
        result = await u.get_id(uuid)
        if not result:
            raise HTTPException(401, {"error": "token tidak bisa diakses"})
        else:
            yield conn, result
    except JWTError as e:
        raise HTTPException(403, {"error": str(e)})
    except IdNotFoundError as e:
        raise HTTPException(404, "id tidak ditemukan")
