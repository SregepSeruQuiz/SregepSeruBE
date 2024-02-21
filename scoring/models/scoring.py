from core.db import meta

from sqlalchemy import Table, Column

from sqlalchemy import BigInteger, Unicode, ForeignKey, SmallInteger

from user.models.user import UserModel
from quiz.models.quizCustomList import QuizCustomListModel


ScoringModel: Table = Table(
    "QuizCustomList", meta,
    Column("id", BigInteger, primary_key=True),
    Column("Custom_ID", None, ForeignKey(QuizCustomListModel.c.id, ondelete="CASCADE")),
    Column("User_ID", None, ForeignKey(UserModel.c.id, ondelete="CASCADE")),
    Column("Score", SmallInteger)
)
