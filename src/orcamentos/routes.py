from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from src.clientes.models import Cliente
from src.database import SessionDep
from src.orcamentos.models import ItemOrcamento, Orcamento
from src.orcamentos.schemas import OrcamentoRead
from src.produtos.models import Produto

orcamentos_router = APIRouter()


# ---------------- ORÇAMENTOS ----------------


@orcamentos_router.post("/", response_model=Orcamento)
def criar_orcamento(
    cliente_id: int,
    itens: List[dict],  # [{'produto_id': 1, 'quantidade': 2}]
    session: SessionDep,
):
    orcamento = Orcamento(cliente_id=cliente_id)
    session.add(orcamento)
    session.commit()
    session.refresh(orcamento)

    for item in itens:
        produto = session.get(Produto, item["produto_id"])
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")

        item_orcamento = ItemOrcamento(
            orcamento_id=orcamento.id,
            produto_id=produto.id,
            quantidade=item["quantidade"],
            preco_unitario=produto.preco_unitario,
        )
        session.add(item_orcamento)

    session.commit()
    session.refresh(orcamento)
    return orcamento


@orcamentos_router.get("/", response_model=List[OrcamentoRead])
def listar_orcamentos(
    session: SessionDep,
    cliente_id: Optional[int] = Query(None),
):
    query = select(Orcamento)

    if cliente_id:
        query = query.where(Orcamento.cliente_id == cliente_id)

    orcamentos = session.exec(query).all()

    # Garantir que os itens estão carregados para calcular o total
    for orc in orcamentos:
        orc.itens  # força o relacionamento a carregar

    return orcamentos


@orcamentos_router.get("/{orcamento_id}", response_model=OrcamentoRead)
def obter_orcamento(orcamento_id: int, session: SessionDep):
    orcamento = session.get(Orcamento, orcamento_id)
    if not orcamento:
        raise HTTPException(status_code=404, detail="Orçamento não encontrado")

    orcamento.itens  # garantir que os itens estão carregados
    return orcamento
