import asyncio

from api.db import engine
from core.db import meta
from quiz import tables as tables_quiz
from scoring import tables as tables_scoring
from user import tables as tables_user


async def main():
    """
    untuk membuat table
    :return:
    """
    async with engine.begin() as conn:

        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all, tables=(tables_quiz + tables_scoring + tables_user))

    await engine.dispose()


if __name__ == '__main__':
    asyncio.run(main())
