from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from jose import jwt

from api.config import cfg
from api.depends.db import get_conn
from api.depends.login import get_uuid
from user.facades.user import User
from user.exceptions import EmailNotFoundError, WrongPasswordError

router_login = APIRouter(tags=['login'])

context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


# belum selesai
@router_login.post("/login")
async def login_email(*, conn: AsyncConnection = Depends(get_conn), data: OAuth2PasswordRequestForm = Depends()):
    """
    Router Login
    """
    u = User(conn)
    try:
        result = await u.login_email(data.username)
        if not result:
            raise EmailNotFoundError
        else:
            cek = context.verify(data.password, result.password)
            if cek:
                token = jwt.encode({"uuid": result.uuid}, cfg.secret)
                return {"access_token": token, "token_type": "bearer"}
            else:
                raise WrongPasswordError
    except EmailNotFoundError as e:
        raise HTTPException(status_code=404, detail="Incorrect username ")
    except WrongPasswordError as e:
        raise HTTPException(status_code=406, detail="Incorrect password")
    except IntegrityError as e:
        raise HTTPException(status_code=404, detail="Email not found ")
