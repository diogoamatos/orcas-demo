from fastapi import FastAPI

from src.database import create_db_and_tables
from src.clientes.routes import clientes_router
from src.produtos.routes import produtos_router
from src.orcamentos.routes import orcamentos_router

app = FastAPI()

app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])
app.include_router(orcamentos_router, prefix="/orcamentos", tags=["Orcamentos"])
app.include_router(produtos_router, prefix="/produtos", tags=["Produtos"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def index():
    return {"message": "Hello World"}
