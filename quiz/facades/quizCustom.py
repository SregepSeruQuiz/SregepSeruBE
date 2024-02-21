import attr
from quiz.models.quizCustomList import QuizCustomListModel
from quiz.models.quizCustom import QuizCustomModel
from quiz.cruds.quizCustom import QuizCustomCrud
from quiz.cruds.QuizCustomList import QuizCustomListCrud
from quiz.schemas.quizCustomList import QuizCustomListAddSchema, QuizCustomListReadByIdSchema
from quiz.schemas.quizCustom import QuizCustomAddSchema, QuizCustomReadSchema
from quiz.exceptions import QuizNotFoundError
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncConnection


@attr.define
class QuizCustom:
    """
    Quiz custom  facade
    """
    conn: AsyncConnection

    async def create_custom_list(self, id: int, data: QuizCustomListAddSchema) -> int:
        """
        untuk membuat custom list
        :param id:
        :param data:
        :return:
        """
        return await QuizCustomListCrud(self.conn).input_quiz_custom_list(id, data)

    async def create_question(self, data: QuizCustomAddSchema) -> int:
        """
        untuk membuat pertanyaan
        :param data:
        :return:
        """
        return await QuizCustomCrud(self.conn).create_quiz(data)

    async def get_quiz_by_id_creator(self, id: int) -> list[QuizCustomListReadByIdSchema]:
        """
        untuk menampilkan quiz apa saaj yg dibuat oleh creator
        :param id:
        :return:
        """
        return await QuizCustomListCrud(self.conn).get_quiz_list_custom_by_id(id)

    async def list_quiz_by_custom_list(self, id: int) -> list[QuizCustomReadSchema]:
        """
        menampilkan quiz berdasarkan custom list semuua pertanyaan
        :param id:
        :return:
        """
        return await QuizCustomCrud(self.conn).list_question(id)

    async def get_quiz_by_id(self, id: int) -> QuizCustomReadSchema:
        """
        untuk melihat quiz berdasarkan id
        :param id:
        :return:
        """
        result = await QuizCustomCrud(self.conn).question_by_id(id)
        if not result:
            raise QuizNotFoundError
        return result

    async def get_quiz_custom(self, id: list[int]) -> QuizCustomReadSchema:
        """
        untuk mengambil soal 1 biji
        :param id:
        :return:
        """
        result = await QuizCustomCrud(self.conn).get_quiz_custom(id)
        if result:
            return result
        raise QuizNotFoundError

    async def edit_quiz_by_id(self, id: int, data: QuizCustomAddSchema) -> bool:
        """
        untuk mengubah isi
        :param id:
        :param data:
        :return:
        """
        return await QuizCustomCrud(self.conn).edit_question(id, data)

    async def delete_custom_quiz_list(self, id: int) -> bool:
        """
        untuk menghapus custom list
        :param id: berdasarkan id yg mau dihapus
        :return:
        """
        return await QuizCustomListCrud(self.conn).delete_quiz_custom_list(id)

    async def delete_question(self, id: int) -> bool:
        """
        untuk menghapus pertanyaan yang ingin dihapus
        :param id: id pertanyaan
        :return:
        """
        return await QuizCustomCrud(self.conn).delete_question(id)
