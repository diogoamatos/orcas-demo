from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

# from src.orcamentos.models import Orcamento

class ClienteBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)


class Cliente(ClienteBase, table=True):
    nome: str
    email: Optional[str] = None

    orcamentos: List["Orcamento"] = Relationship(back_populates="cliente")
