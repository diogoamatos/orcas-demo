from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.orcamentos.models import ItemOrcamento


class ProdutoBase(SQLModel):
    nome: str
    preco_unitario: float


class Produto(ProdutoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    itens_orcamento: List["ItemOrcamento"] = Relationship(back_populates="produto")
