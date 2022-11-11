from fastapi import FastAPI
from routes.users import users
from routes.auth import auth
from routes.reviews import reviews
import uvicorn
app = FastAPI()

app.include_router(users)
app.include_router(auth)
app.include_router(reviews)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)