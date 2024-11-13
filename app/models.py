from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    email: EmailStr
    full_name: str

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
