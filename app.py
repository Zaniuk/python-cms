from fastapi import FastAPI
from routes.users import users
from routes.auth import auth
import uvicorn
app = FastAPI()

app.include_router(users)
app.include_router(auth)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)