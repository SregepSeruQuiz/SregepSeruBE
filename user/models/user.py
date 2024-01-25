from core.core import meta

from sqlalchemy import Table, Column

from sqlalchemy import BigInteger, Unicode, Boolean

UserModel: Table = Table(
    "User", meta,
    Column("id", BigInteger, primary_key=True),
    Column("uuid", Unicode(256), nullable=False, unique=True),
    Column("username", Unicode(256), nullable=False, unique=True),
    Column("email", Unicode(256), nullable=False, unique=True),
    Column("password", Unicode(256), nullable=False, unique=True),
    Column("reviewer", Unicode(256), nullable=False, default="NonReviewer")
)
