from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Product(BaseModel):
    name: str
    description: str
    seller_id: int
    price: int
    created_at: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    updated_at: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    