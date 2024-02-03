from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncConnection
from api.db import engine


async def get_conn() -> AsyncIterator[AsyncConnection]:
    """
    buat transcaction
    :return:
    """
    async with engine.begin() as conn:
        yield conn
