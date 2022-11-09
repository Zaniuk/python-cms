from fastapi import APIRouter, Header , Request

auth = APIRouter()

@auth.post("/auth/login")
def login(request : Request):
    header = request.headers['Authorization'] or request.headers['authorization'] 
    return {"message": "Login successful", "Authorization": header}

@auth.post("/auth/register")
def register():
    return {"message": "Registration successful"}