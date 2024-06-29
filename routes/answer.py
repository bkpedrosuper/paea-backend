from fastapi import APIRouter
from models.answer import Answer
from config.database import answer_collection
from schema.answer_schema import list_serializer as form_answer_list_serializer
from bson import ObjectId

router = APIRouter()

# Get all form answers from form_id
@router.get("/form_answers/{form_id}")
async def get_form_answers(form_id: str):
    form_answers = answer_collection.find({"form_id": form_id})
    return form_answer_list_serializer(form_answers)

# Post a new form answer
@router.post("/answer")
async def post_form_answer(answer: Answer):
    new_answer = answer_collection.insert_one(dict(answer))
    return {"message": "Form answer created successfully", "answer_id": str(new_answer.inserted_id)}
