from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["Project0"]
users_collection = db["abhi-2212"]
