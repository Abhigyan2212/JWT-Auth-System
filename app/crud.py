from app.models import User, UserCreate
from app.database import users_collection
from bson import ObjectId

async def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["password"] = user_dict["password"]  # Password should be hashed
    result = await users_collection.insert_one(user_dict)
    return str(result.inserted_id)

async def get_user_by_email(email: str):
    user = await users_collection.find_one({"email": email})
    return user

async def get_user(user_id: str):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    return user

async def update_user(user_id: str, user: User):
    user_dict = user.dict(exclude_unset=True)
    await users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})

async def delete_user(user_id: str):
    await users_collection.delete_one({"_id": ObjectId(user_id)})
