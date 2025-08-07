from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ProdutoRead(BaseModel):
    id: int
    nome: str
    preco_unitario: float

    class Config:
        orm_mode = True
