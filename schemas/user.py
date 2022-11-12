from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
    createdAt: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    updatedAt: str = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    