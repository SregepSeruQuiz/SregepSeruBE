import attr
from quiz.models.QuizUmum import QuizUmumModel
from quiz.schemas.QuizUmum import QuizUmumReadSchema, PaginationSchema
from quiz.cruds.QuizUmum import QuizUmumCrud
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncConnection
from quiz.exceptions import QuizNotFoundError


@attr.define
class QuizUmum:
    """
    Quiz UMUM  facade
    """
    conn: AsyncConnection

    async def get_quiz_umum(self, id: list[int]) -> QuizUmumReadSchema:
        """
        get quiz umum
        :param id:
        :return:
        """
        result = await QuizUmumCrud(self.conn).get_quiz_umum(id)
        if result:
            return result
        raise QuizNotFoundError
