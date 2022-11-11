from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from models.user import user
from schemas.user import User

users = APIRouter()

@users.get("/users")
def get_users():
    try:
        return conn.execute(user.select()).fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@users.get("/users/{user_id}")
async def get_user(user_id: int) -> Response:
    
    try:
        query = user.select().where(user.c.id == user_id)
        result = conn.execute(query).fetchone()
        if type(result) == None or result == None:
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
        

@users.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        return conn.execute(user.delete().where(user.c.id == user_id))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@users.put("/users/{user_id}")
def update_user(User:User, user_id: int):
    try:
        pass        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    