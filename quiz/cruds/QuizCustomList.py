import attr
import cattr
from sqlalchemy.ext.asyncio import AsyncConnection

from sqlalchemy import select
from quiz.models.QuizCustomList import QuizCustomListModel
from quiz.schemas.QuizCustomList import QuizCustomListReadByIdSchema, QuizCustomListAddSchema


@attr.define
class QuizCustomListCrud:
    """
    crud untuk user
    """
    conn: AsyncConnection

    async def get_quiz_list_custom_by_id(self, id: int) -> list[QuizCustomListReadByIdSchema]:
        """
            untuuk melihat list quiz custom yg dibuat oleh id custom berikut
        """
        query = select(QuizCustomListModel.c.id, QuizCustomListModel.c.Genre,
                       QuizCustomListModel.c.Description).select_from(QuizCustomListModel).where(
            QuizCustomListModel.c.User_ID == id)
        result = await self.conn.execute(query)
        return cattr.structure(
            (row._mapping for row in result),
            list[QuizCustomListReadByIdSchema]
        )

    async def input_quiz_custom_list(self, id: int, data: QuizCustomListAddSchema) -> int:
        """
            untuk input list quiz
        :param id:
        :param data:
        :return:
        """
        query = QuizCustomListModel.insert().values(User_ID=id, **data.dict())
        result = await self.conn.execute(query)
        return result.inserted_primary_key[0]

    async def delete_quiz_custom_list(self, id: int) -> bool:
        """
        delete quiz custom list
        :param id:
        :return:
        """
        query = QuizCustomListModel.delete().where(QuizCustomModel.c.id == id)
        await self.conn.execute(query)
        return True
