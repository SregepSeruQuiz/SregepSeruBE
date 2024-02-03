from typing import Optional

import attr
import cattr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection
from scoring.models.scoring import ScoringModel
from user.models.user import UserModel
from scoring.schemas.scoring import ScoringAddSchema,ScoringReadSchema

@attr.define
class ScoringCrud:
    """
    crud untuk scoring
    """
    conn: AsyncConnection
    async def input_scoring(self,id:int,data:ScoringAddSchema)-> int:
        """
        input data untuk scoring
        :param id:
        :param data:
        :return:
        """
        query = ScoringModel.insert().values(id=id,**data.dict())
        result = await self.conn.execute(query)
        return result.inserted_primary_key[0]
    async def get_list_scoring(self,custom_id:int)-> list[ScoringReadSchema]:
        """
        membaca scoring untuk pembuat
        :param custom_id:
        :return:
        """
        query=select(ScoringModel.c.id,ScoringModel.c.Custom_id,UserModel.c.nama,ScoringModel.c.Score).select_from(ScoringModel.join(UserModel)).where(ScoringModel.c.Custom_id==custom_id)
        result = await self.conn.execute(query)
        return cattr.structure(
            (row._mapping for row in result),
            list[ScoringReadSchema]
        )