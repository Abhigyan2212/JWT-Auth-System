from fastapi import FastAPI
from app import auth, crud, database
from app.models import User, UserCreate

app = FastAPI()

app.include_router(auth.router)
app.include_router(crud.router)
