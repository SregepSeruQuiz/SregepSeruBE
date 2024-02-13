import re
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncConnection

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


@router_quizcustom.post("/create_question")
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


@router_quizcustom.get("/get_quiz_by_id_creator")
async def get_quiz_by_id_creator(*, conn_id: AsyncConnection = Depends(get_user_id)):
    """
    untuk menampilkan quiz apa saaj yg dibuat oleh creator
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = QuizCustom(conn)
    result = await u.get_quiz_by_id_creator(id)
    return result


@router_quizcustom.get("/list_quiz_by_custom_list")
async def list_quiz_by_custom_list(*, conn_id: AsyncConnection = Depends(get_user_id)):
    """
    menampilkan quiz berdasarkan custom list semuua pertanyaan
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = QuizCustom(conn)
    result = await u.list_quiz_by_custom_list(id)
    return result


@router_quizcustom.get("/get_quiz_by_id")
async def get_quiz_by_id(*, conn_id: AsyncConnection = Depends(get_user_id)):
    """
    untuk melihat quiz berdasarkan id
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = QuizCustom(conn)
    result = await u.get_quiz_by_id(id)
    return result


@router_quizcustom.get("/get_quiz_custom")
async def get_quiz_custom(*, conn_id: AsyncConnection = Depends(get_user_id)):
    """
    untuk mengambil soal 1 biji
    :param conn_id:
    :param email:
    :return:
    """
    conn = conn_id[0]
    id = conn_id[1]
    u = QuizCustom(conn)
    result = await u.get_quiz_custom(id)
    return result


@router_quizcustom.put("/edit_quiz_by_id")
async def edit_quiz_by_id(*, conn_id: AsyncConnection = Depends(get_user_id), data: QuizCustomAddSchema):
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
    result = await u.edit_quiz_by_id(id, data)
    return result


@router_quizcustom.delete("/delete_custom_quiz_list")
async def delete_custom_quiz_list(*, conn_id: AsyncConnection = Depends(get_user_id)):
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
    result = await u.delete_custom_quiz_list(id)
    return result


@router_quizcustom.delete("/delete_question")
async def delete_question(*, conn_id: AsyncConnection = Depends(get_user_id)):
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
    result = await u.delete_question(id)
    return result
