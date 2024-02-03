import attr
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncConnection
from scoring.cruds.scoring import ScoringCrud
from scoring.schemas.scoring import ScoringReadSchema,ScoringAddSchema
@attr.define
class Scoring:
    """
    Scoring
    """
    conn: AsyncConnection
    async def input_score(self,id:int,data:ScoringAddSchema)->int:
        """
        input data
        :param id:
        :param data:
        :return:
        """
        return await ScoringCrud(self.conn).input_scoring(id,data)
    async def list_score(self,custom_id:int)->list[ScoringReadSchema]:
        """
        list score
        :param custom_id:
        :return:
        """
        return await ScoringCrud(self.conn).get_list_scoring(custom_id)