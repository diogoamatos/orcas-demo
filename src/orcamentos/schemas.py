from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from src.produtos.schemas import ProdutoRead
from src.clientes.schemas import ClienteRead


class ItemOrcamentoRead(BaseModel):
    produto: ProdutoRead
    quantidade: int
    preco_unitario: float

    class Config:
        orm_mode = True


class OrcamentoRead(BaseModel):
    id: int
    data: datetime
    cliente: Optional[ClienteRead]
    itens: List[ItemOrcamentoRead]
    total: float  # calculado manualmente no endpoint

    class Config:
        orm_mode = True
