import attr
from pydantic import BaseModel, Field, validator
from user.exceptions import BelowZeroError
from enum import Enum

@attr.define(slots=False)
class ScoringReadSchema:
    """
    Melihat Informasi User
    """
    id:int
    Custom_ID:int
    nama: str
    Score:int

class ScoringAddSchema(BaseModel):
    """
    untuk input scoring
    """
    Custom_ID:int
    Score:int
