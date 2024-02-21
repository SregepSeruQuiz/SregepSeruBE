import attr
from pydantic import BaseModel, Field, validator
from user.exceptions import BelowZeroError
from enum import Enum
@attr.define(slots=False)
class QuizCustomListReadByIdSchema:
    """
    Melihat list custom quiz yg dibuat oleh id berikut
    """
    id :int
    Genre: str
    Description :str

class QuizCustomListAddSchema(BaseModel):
    Genre:str
    Description:str