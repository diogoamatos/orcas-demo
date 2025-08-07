from typing import List

from fastapi import APIRouter
from sqlmodel import select

from src.clientes.models import Cliente
from src.database import SessionDep

clientes_router = APIRouter()
# ---------------- CLIENTES ----------------


@clientes_router.post("/", response_model=Cliente)
def criar_cliente(cliente: Cliente, session: SessionDep):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente


@clientes_router.get("/", response_model=List[Cliente])
def listar_clientes(session: SessionDep):
    return session.exec(select(Cliente)).all()
