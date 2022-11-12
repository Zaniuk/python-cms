from fastapi import FastAPI
from routes.users import users
from routes.auth import auth
from routes.products import products
from routes.reviews import reviews
from routes.orders import orders
import uvicorn
app = FastAPI()

app.include_router(users)
app.include_router(auth)
app.include_router(products)
app.include_router(reviews)
app.include_router(orders)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)