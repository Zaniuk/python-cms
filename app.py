from fastapi import FastAPI
from routes.users import users
from routes.auth import auth
from routes.reviews import reviews
from routes.products import products
import uvicorn
app = FastAPI()

app.include_router(users)
app.include_router(auth)
app.include_router(reviews)
app.include_router(products)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)