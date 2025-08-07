from typing import List

from fastapi import APIRouter
from sqlmodel import select

from src.clientes.models import ClienteBase, Cliente
from src.database import SessionDep

clientes_router = APIRouter()
# ---------------- CLIENTES ----------------


@clientes_router.post("/", response_model=Cliente)
def criar_cliente(cliente: ClienteBase, session: SessionDep):
    novo_cliente = Cliente(nome=cliente.nome, email=cliente.email)
    session.add(novo_cliente)
    session.commit()
    session.refresh(novo_cliente)
    return novo_cliente


@clientes_router.get("/", response_model=List[Cliente])
def listar_clientes(session: SessionDep):
    return session.exec(select(Cliente)).all()
