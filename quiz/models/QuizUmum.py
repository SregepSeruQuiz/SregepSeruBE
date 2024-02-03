from core.db import meta

from sqlalchemy import Table, Column

from sqlalchemy import BigInteger, Unicode

QuizUmumModel: Table = Table(
    "QuizUmum", meta,
    Column("id", BigInteger, primary_key=True),
    Column("Category", Unicode(256), nullable=False, unique=True),
    Column("Question", Unicode(256), nullable=False, unique=True),
    Column("Answer", Unicode(256), nullable=False, unique=True),
)
