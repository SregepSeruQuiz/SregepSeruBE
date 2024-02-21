import attr
from pydantic import BaseModel, Field, validator
from user.exceptions import BelowZeroError
from enum import Enum

@attr.define(slots=False)
class QuizCustomReadSchema:
    """
    membaca list soal
    """
    id: int
    Custom_ID: int
    Question: str
    Score: int
    Answer: str

class QuizCustomAddSchema(BaseModel):
    Custom_ID: int
    Question: str
    Score: int
    Answer: str
