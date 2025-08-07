from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from src.orcamentos.models import ItemOrcamento
class ProdutoBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)


class Produto(ProdutoBase, table=True):
    nome: str
    preco_unitario: float

    itens_orcamento: List["ItemOrcamento"] = Relationship(back_populates="produto")
