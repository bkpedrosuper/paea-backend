from fastapi import APIRouter
from models.form import Form
from config.database import form_collection
from schema.form_schema import list_serializer as form_list_serializer, serializer
from bson import ObjectId

router = APIRouter()

# Post form
@router.post("/form")
async def post_form(form: Form):
    form_id = form_collection.insert_one(dict(form)).inserted_id
    return {"form_id": str(form_id)}

@router.get("/form/{form_id}")
async def get_form(form_id: str):
    form = form_collection.find_one({"_id": ObjectId(form_id)})
    return serializer(form)

@router.get("/forms")
async def get_forms():
    forms = form_collection.find()
    print(forms)
    return form_list_serializer(forms)