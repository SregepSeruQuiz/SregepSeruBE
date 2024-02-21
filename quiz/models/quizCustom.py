from core.db import meta

from sqlalchemy import Table, Column

from sqlalchemy import BigInteger, Unicode, ForeignKey, SmallInteger

from quiz.models.quizCustomList import QuizCustomListModel

QuizCustomModel: Table = Table(
    "QuizCustom", meta,
    Column("id", BigInteger, primary_key=True),
    Column("Custom_ID", None, ForeignKey(QuizCustomListModel.c.id, ondelete="CASCADE")),
    Column("Question", Unicode(256), nullable=False, unique=True),
    Column("Score", SmallInteger),
    Column("Answer", Unicode(256), nullable=False, unique=True),
)
