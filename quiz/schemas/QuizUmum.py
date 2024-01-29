import attr
from pydantic import BaseModel, Field, validator
from user.exceptions import BelowZeroError
from enum import Enum


@attr.define(slots=False)
class QuizUmumReadSchema:
    """
    Melihat Quiz
    """
    id: int
    Question: str
    Answer: str


class PaginationSchema(BaseModel):
    """
    PaginationSchema setting
    """
    page_number: int
    size: int
    order: str = "asc"

    @validator('page_number', 'size')
    def check_negative(cls, value):
        if value <= 0:
            raise BelowZeroError
        return value
