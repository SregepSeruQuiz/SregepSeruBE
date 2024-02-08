import attr
from pydantic import BaseModel, Field, validator
from user.exceptions import BelowZeroError
from enum import Enum


# Jaga2 kalo butuh dipake
class StatusReviewerEnum(str, Enum):
    """
    Status Reviewer
    """
    Reviewer = "Reviewer"
    NonReviewer = "NonReviewer"


@attr.define(slots=False)
class UserReadSchema:
    """
    Melihat Informasi User
    """
    username: str
    nama: str
    email: str


@attr.define(slots=False)
class LoginSchema:
    """
    Melihat Informasi User
    """
    uuid: str
    password: str


class UserAddSchema(BaseModel):
    username: str
    nama: str
    email: str = Field(regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    password: str=Field(regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$')
    reviewer: StatusReviewerEnum = Field(StatusReviewerEnum.NonReviewer)


class UpdateEmailSchema(BaseModel):
    email: str = Field(regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
class UpdatePasswordSchema(BaseModel):
    password: str = Field(regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$')

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
