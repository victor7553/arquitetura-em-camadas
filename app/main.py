# app/main.py
from fastapi import FastAPI
from app.core.database import engine  # Conexão com o banco
from app.api.v1.hero_routes import router as hero_router  # Suas rotas

# Cria a instância principal do aplicativo FastAPI
app = FastAPI(
    title="API de Heróis",
    version="1.0.0",
    description="API exemplo usando FastAPI + SQLModel",
)

# Evento que roda quando o app inicia
@app.on_event("startup")
def on_startup():
    # Teste simples para verificar se o banco conecta
    with engine.connect() as connection:
        print("✅ Banco de dados conectado com sucesso!")

# Inclui as rotas da versão 1 da API
app.include_router(hero_router, prefix="/api/v1", tags=["Heróis"])

# Rota raiz simples
@app.get("/")
def root():
    return {"message": "API FastAPI está rodando!"}
