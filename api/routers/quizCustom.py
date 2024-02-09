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
from api.depends.login import get_user_id
from quiz.facades.QuizCustom import QuizCustom
from quiz.schemas.QuizCustom import QuizCustomAddSchema, QuizCustomReadSchema
from quiz.schemas.QuizCustomList import QuizCustomListAddSchema, QuizCustomListReadByIdSchema

router_quizcustom = APIRouter(tags=['custom'])


@router_quizcustom.post("/customlist")
async def create_custom_list(*, conn_id: AsyncConnection = Depends(get_user_id), data: QuizCustomListAddSchema):
    """
    create custom list
    :param data:
    :param conn_id:
    :param conn:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = QuizCustom(conn)
    result = await u.create_custom_list(id, data)
    return result


@router_quizcustom.post("/custom")
async def create_question(*, conn_id: AsyncConnection = Depends(get_user_id), data: QuizCustomAddSchema):
    """
    create question
    :param data:
    :param conn_id:
    :param conn:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = QuizCustom(conn)
    result = await u.create_question(data)
    return result


@router_quizcustom.put("/update_email")
async def update_email(*, conn_id: AsyncConnection = Depends(get_user_id), email: UpdateEmailSchema):
    """
    router untuk change email
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = User(conn)
    result = await u.update_email(id, email)
    return result


@router_quizcustom.put("/update_password")
async def update_password(*, conn_id: AsyncConnection = Depends(get_user_id), password: UpdatePasswordSchema):
    """
    router untuk change email
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = User(conn)
    result = await u.update_password(id, password)
    return result
