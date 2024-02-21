import attr
import cattr
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncConnection

from sqlalchemy import select
from quiz.models.quizUmum import QuizUmumModel
from quiz.schemas.quizUmum import QuizUmumReadSchema


@attr.define
class QuizUmumCrud:
    """
    Crud untuk QuizUmum
    """
    conn: AsyncConnection

    async def get_quiz_umum(self, id: list[int]) -> Optional[QuizUmumReadSchema]:
        """
        get quiz umum
        :param id:
        :return:
        """
        query = select(QuizUmumModel.c.id, QuizUmumModel.c.Question, QuizUmumModel.c.Answer).select_from(QuizUmumModel).where(
            QuizUmumModel.c.id != id).limit(1)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, QuizUmumReadSchema)
        return None
