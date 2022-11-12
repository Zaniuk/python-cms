from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Order(BaseModel):
    product_id: int
    seller_id: int
    user_id : int
    created_at: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    updated_at: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    