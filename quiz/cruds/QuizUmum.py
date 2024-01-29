import attr
import cattr
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncConnection

from sqlalchemy import select
from quiz.models.QuizUmum import QuizUmumModel
from quiz.schemas.QuizUmum import QuizUmumReadSchema


@attr.define
class QuizUmumReadCrud:
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
        query = select(QuizUmumModel.c.id, QuizUmumModel.c.Question, QuizUmumModel.c.Answer).where(
            QuizUmumModel.c.id != id).limit(1)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, QuizUmumReadSchema)
        return None
