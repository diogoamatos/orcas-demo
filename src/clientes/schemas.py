from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ClienteRead(BaseModel):
    id: int
    nome: str
    email: Optional[str] = None

    class Config:
        orm_mode = True
