from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.orcamentos.models import Orcamento

class ClienteBase(SQLModel):
    nome: str
    email: Optional[str] = None


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    orcamentos: List["Orcamento"] = Relationship(back_populates="cliente")
