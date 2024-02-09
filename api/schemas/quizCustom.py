from pydantic import BaseModel

class QuizCustomRouterAddSchema(BaseModel):
    Custom_ID: int
    Question: str
    Score: int
    Answer: str