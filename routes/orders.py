from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from models.order import order
from schemas.order import Order

orders = APIRouter()

@orders.post("/orders", status_code=status.HTTP_201_CREATED, tags=["Orders"])
def create_order(Order: Order):
    try: 
        conn.execute(order.insert().values(Order.dict()))
        return Order
    except Exception as e:
        print(e.__dict__)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
    
@orders.get('/orders', status_code=status.HTTP_200_OK, tags=["Orders"])
def get_orders():
    try:
        return conn.execute(order.select()).fetchall()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
@orders.get('/orders/{id}', status_code=status.HTTP_200_OK, tags=["Orders"])
def get_order(id: int):
    try:
        return conn.execute(order.select().where(order.c.id == id)).fetchone()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
@orders.get('orders/{user_id}', status_code=status.HTTP_200_OK, tags=["Orders"])
def get_user_orders(user_id: int):
    try:
        return conn.execute(order.select().where(order.c.user_id == user_id)).fetchall()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
    
@orders.get('orders/{product_id}', status_code=status.HTTP_200_OK, tags=["Orders"])
def get_product_orders(product_id: int):
    try:
        return conn.execute(order.select().where(order.c.product_id == product_id)).fetchall()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")