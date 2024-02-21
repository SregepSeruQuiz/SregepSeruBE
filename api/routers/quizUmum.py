from fastapi import APIRouter
from fastapi import Depends, HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncConnection

from typing import Optional

from quiz.facades.quizUmum import QuizUmum
from quiz.schemas.quizUmum import QuizUmumReadSchema
from quiz.exceptions import QuizNotFoundError
from api.depends.login import get_user_id
from api.depends.db import get_conn

router_quizumum = APIRouter(prefix="/quiz", tags=["QuizUmum"])


@router_quizumum.get("/umum", tags=["umum"])
async def get_quiz_umum(*, conn=Depends(get_conn), id: list[int]):
    """
    Quiz Umum
    :param conn:
    :return:
    """
    u = QuizUmum(conn)
    try:
        result = await u.get_quiz_umum(id)
        return result
    except QuizNotFoundError as e:
        raise HTTPException(status_code=404, detail="Quiz not found ")


