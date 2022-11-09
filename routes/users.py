from fastapi import APIRouter

users = APIRouter()

@users.get("/users")
def get_users():
    return [{"name": "John"}, {"name": "Jane"}]

@users.get("/users/{user_id}")
def get_user(user_id: int):
    return {"name": "John Doe", "id": user_id}

@users.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"name": "John Doe", "id": user_id}

@users.put("/users/{user_id}")
def update_user(user_id: int):
    return {"name": "John Doe", "id": user_id}
