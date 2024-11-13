from fastapi import APIRouter, Depends, HTTPException
from app.models import Token, User, UserLogin
from app.utils import create_access_token, verify_password
from app.database import users_collection
from app.crud import get_user_by_email
from pydantic import BaseModel

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    user = await get_user_by_email(user_login.email)
    if not user or not verify_password(user_login.password, user['password']):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/logout")
async def logout():
    return {"message": "Logout successful"}
