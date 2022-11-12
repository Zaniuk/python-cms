
from fastapi import APIRouter, Response, Request, status, HTTPException
from config.db import conn
from models.user import user
from schemas.user import User
auth = APIRouter()

@auth.post("/auth/login", tags=["Auth"])
def login(request : Request, user : User):
    
    header = request.headers['Authorization'] or request.headers['authorization'] 
    return {"message": "Login successful", "Authorization": header}

@auth.post("/auth/register", tags=["Auth"])
def register( User : User):
    #req = request.body
    new_user = {
        "name": User.name,
        "email": User.email,
        "password": User.password
    }
    try:
        conn.execute(user.insert().values(new_user))
        return User
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))