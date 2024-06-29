from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import os
load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri)

db = client.paea

answer_collection = db["answers"]
form_collection = db["forms"]