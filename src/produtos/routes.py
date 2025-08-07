from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from src.database import SessionDep
from src.orcamentos.models import ItemOrcamento
from src.produtos.models import ProdutoBase, Produto

produtos_router = APIRouter()
# ---------------- PRODUTOS ----------------


@produtos_router.post("/", response_model=Produto)
def criar_produto(produto: ProdutoBase, session: SessionDep):
    novo_produto = Produto(nome=produto.nome, preco_unitario=produto.preco_unitario)
    session.add(novo_produto)
    session.commit()
    session.refresh(novo_produto)
    return novo_produto


@produtos_router.get("/", response_model=List[Produto])
def listar_produtos(session: SessionDep):
    return session.exec(select(Produto)).all()
