import attr
import cattr
from sqlalchemy.ext.asyncio import AsyncConnection
from typing import Optional

from sqlalchemy import select
from quiz.models.quizCustomList import QuizCustomListModel
from quiz.models.quizCustom import QuizCustomModel
from quiz.schemas.quizCustom import QuizCustomAddSchema, QuizCustomReadSchema


@attr.define
class QuizCustomCrud:
    """
    crud untuk quiz custom
    """
    conn: AsyncConnection

    async def create_quiz(self, data: QuizCustomAddSchema) -> int:
        """
        untuk add quiz beradasarkan custom id
        """
        query = QuizCustomModel.insert().values(**data.dict())
        result = await self.conn.execute(query)
        return result.inserted_primary_key[0]

    async def list_question(self, id_custom_list: int) -> list[QuizCustomReadSchema]:
        """
        untuk melihhat list semua soal
        :param id_custom_list:
        :return:
        """
        query = select(QuizCustomModel.c.id, QuizCustomModel.c.Custom_ID, QuizCustomModel.c.Question,
                       QuizCustomModel.c.Score, QuizCustomModel.c.Answer).select_from(QuizCustomModel).where(
            QuizCustomModel.c.Custom_ID == id_custom_list)
        result = await self.conn.execute(query)
        return cattr.structure(
            (row._mapping for row in result),
            list[QuizCustomReadSchema]
        )

    async def question_by_id(self, id: int) -> Optional[QuizCustomReadSchema]:
        """
        untuk melihhat list semua soal
        :param id_custom_list:
        :return:
        """
        query = select(QuizCustomModel.c.id, QuizCustomModel.c.Custom_ID, QuizCustomModel.c.Question,
                       QuizCustomModel.c.Score, QuizCustomModel.c.Answer).select_from(QuizCustomModel).where(
            QuizCustomModel.c.id == id)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, QuizCustomReadSchema)
        return None

    async def get_quiz_custom(self, id: list[int]) -> Optional[QuizCustomReadSchema]:
        """
        get quiz custom untuk soal
        :param id:
        :return:
        """
        query = select(QuizCustomModel.c.id, QuizCustomModel.c.Custom_ID, QuizCustomModel.c.Question,
                       QuizCustomModel.c.Score, QuizCustomModel.c.Answer).select_from(
            QuizCustomModel).where(QuizCustomModel.c.id != id).limit(1)
        result = (await self.conn.execute(query)).first()
        if result:
            return cattr.structure(result._mapping, QuizCustomReadSchema)
        return None

    async def edit_question(self, id: int, data: QuizCustomAddSchema) -> bool:
        """
        update soal
        :param id:
        :param data:
        :return:
        """
        query = QuizCustomModel.update().where(QuizCustomModel.c.id == id)
        query = query.values(Question=data.Question, Score=data.Score, Answer=data.Answer)
        await self.conn.execute(query)
        return True

    async def delete_question(self, id: int) -> bool:
        """
        delete pertanyaan
        :param id:
        :return:
        """
        query = QuizCustomModel.delete().where(QuizCustomModel.c.id == id)
        await self.conn.execute(query)
        return True
