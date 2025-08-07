from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.clientes.models import Cliente
from src.produtos.models import Produto


class OorcamentoBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)


class Orcamento(OorcamentoBase, table=True):
    data: datetime = Field(default_factory=datetime.utcnow)
    cliente_id: Optional[int] = Field(default=None, foreign_key="cliente.id")

    cliente: Optional[Cliente] = Relationship(back_populates="orcamentos")
    itens: List["ItemOrcamento"] = Relationship(back_populates="orcamento")

    @property
    def total(self) -> float:
        return sum(item.quantidade * item.preco_unitario for item in self.itens)


class ItemOrcamento(SQLModel, table=True):
    orcamento_id: Optional[int] = Field(
        default=None, foreign_key="orcamento.id", primary_key=True
    )
    produto_id: Optional[int] = Field(
        default=None, foreign_key="produto.id", primary_key=True
    )

    quantidade: int
    preco_unitario: (
        float  # Captura o preço no momento do orçamento (pode variar do produto atual)
    )

    orcamento: Orcamento = Relationship(back_populates="itens")
    produto: Produto = Relationship(back_populates="itens_orcamento")
