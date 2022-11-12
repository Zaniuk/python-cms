from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Review(BaseModel):
    name: str
    description: str
    product_id: int
    user_id: int
    createdAt: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    updatedAt: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    