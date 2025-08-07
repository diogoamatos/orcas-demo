from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from src.database import SessionDep
from src.orcamentos.models import ItemOrcamento, Orcamento
from src.produtos.models import Produto

produtos_router = APIRouter()
# ---------------- PRODUTOS ----------------


@produtos_router.post("/", response_model=Produto)
def criar_produto(produto: Produto, session: SessionDep):
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto


@produtos_router.get("/", response_model=List[Produto])
def listar_produtos(session: SessionDep):
    return session.exec(select(Produto)).all()
