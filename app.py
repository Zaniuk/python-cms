from fastapi import FastAPI
from routes.users import users
from routes.auth import auth
app = FastAPI()

app.include_router(users)
app.include_router(auth)