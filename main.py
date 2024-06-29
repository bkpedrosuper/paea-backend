from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from routes.answer import router as answer_router
from routes.form import router as form_router
load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(answer_router)
app.include_router(form_router)
