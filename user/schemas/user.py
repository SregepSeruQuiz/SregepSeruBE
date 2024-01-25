import attr
from pydantic import BaseModel, Field
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
    id: int
    username: str
    email: str


class UserAddSchema(BaseModel):
    username: str
    email: str = Field(regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    password: str


class UserUpdateStatusSchema(BaseModel):
    reviewer: StatusReviewerEnum = Field(StatusReviewerEnum)
