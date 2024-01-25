from core.core import meta

from sqlalchemy import Table, Column

from sqlalchemy import BigInteger, Unicode, ForeignKey

from user.models.user import UserModel

QuizCustomListModel: Table = Table(
    "QuizCustomList", meta,
    Column("id", BigInteger, primary_key=True),
    Column("User_ID", None, ForeignKey(UserModel.c.id, ondelete="CASCADE")),
    Column("Genre", Unicode(256), nullable=False, unique=True),
    Column("Description", Unicode(256), nullable=False, unique=True),
)
