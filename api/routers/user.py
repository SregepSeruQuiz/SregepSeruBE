import re
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
from api.depends.login import get_user_id
from user.facades.user import User
from user.exceptions import EmailNotFoundError, WrongPasswordError
from user.schemas.user import UserAddSchema,UpdateEmailSchema,UpdatePasswordSchema
router_login = APIRouter(tags=['login'])

context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# belum selesai
@router_login.post("/login")
async def login(*, conn: AsyncConnection = Depends(get_conn), data: OAuth2PasswordRequestForm = Depends()):
    """
    Router Login
    """
    u = User(conn)
    try:
        if re.fullmatch(regex, data.username):
            result = await u.login_email(data.username)
        else:
            result = await u.login_username(data.username)
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

@router_login.post("/create_user")
async def create_user(*,conn: AsyncConnection = Depends(get_conn), data:UserAddSchema):
    """
    router untuk membuat user baru
    :param conn:
    :param data:
    :return:
    """
    u = User(conn)
    try:
        result = await u.input(data)
        return result
    except IntegrityError as e:
        raise HTTPException(status_code=404, detail="Email not found ")

@router_login.post("/profile")
async def profile(*,conn_id:AsyncConnection = Depends(get_user_id)):
    """
    router untuk melihat profile diri sendiri
    :param conn:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = User(conn)
    result = await u.profile(id)
    return result

@router_login.update("/update_email")
async def update_email(*,conn_id:AsyncConnection = Depends(get_user_id),email:UpdateEmailSchema):
    """
    router untuk change email
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = User(conn)
    result = await u.update_email(id,email)
    return result
@router_login.update("/update_password")
async def update_password(*,conn_id:AsyncConnection = Depends(get_user_id),password:UpdatePasswordSchema):
    """
    router untuk change email
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = User(conn)
    result = await u.update_password(id,password)
    return result
