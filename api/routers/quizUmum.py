from fastapi import APIRouter
from fastapi import Depends, HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncConnection

from typing import Optional

from quiz.exceptions import QuizNotFoundError
from api.depends.login import get_user_id

router_quiz = APIRouter(prefix="/quiz", tags=["Quiz"])


