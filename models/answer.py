from pydantic import BaseModel

class Answer(BaseModel):
    question: str
    question_number: int
    answer: str
    type: str
    form_id: str
    user: str
    points: int