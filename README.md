# ⚡ FastAPI + SQLModel — Arquitetura em Camadas com Princípios de DDD

Este projeto foi desenvolvido em **Python** com o framework **FastAPI** e o ORM **SQLModel**, seguindo uma **arquitetura em camadas** inspirada nos **princípios de Domain-Driven Design (DDD)**.

Essa estrutura organiza o código em módulos bem definidos, facilitando **manutenção, escalabilidade e reuso** de componentes.

---

## 🚀 Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** → Framework moderno e rápido para criação de APIs.
- **[SQLModel](https://sqlmodel.tiangolo.com/)** → ORM que combina o poder do SQLAlchemy com a validação do Pydantic.
- **[Uvicorn](https://www.uvicorn.org/)** → Servidor ASGI leve e rápido.
- **[Pydantic](https://docs.pydantic.dev/)** → Validação e tipagem robusta de dados.
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** → Leitura de variáveis de ambiente.

---

## 🏗️ Estrutura de Pastas

Abaixo está o modelo de diretórios baseado na **arquitetura em camadas** com princípios de DDD:

project/
│
├── app/                              # 🧠 Núcleo da aplicação
│   ├── __init__.py
│   │
│   ├── main.py                       # 🚀 Ponto de entrada do FastAPI
│   │
│   ├── core/                         # ⚙️ Configurações e infraestrutura
│   │   ├── __init__.py
│   │   ├── config.py                 # Configurações (variáveis, .env)
│   │   ├── database.py               # Engine, sessão e conexão SQLModel
│   │   ├── security.py               # (opcional) JWT, autenticação, senhas
│   │   └── logging.py                # Configuração de logs e middlewares
│   │
│   ├── models/                       # 🧱 Modelos do domínio (tabelas SQLModel)
│   │   ├── __init__.py
│   │   ├── hero.py                   # Exemplo: modelo Hero
│   │   ├── user.py                   # Exemplo: modelo User
│   │   └── product.py                # Exemplo: modelo Product
│   │
│   ├── schemas/                      # 📦 Schemas de entrada e saída (DTOs)
│   │   ├── __init__.py
│   │   ├── hero_schema.py
│   │   ├── user_schema.py
│   │   └── product_schema.py
│   │
│   ├── crud/                         # 💾 Acesso ao banco (Create, Read, Update, Delete)
│   │   ├── __init__.py
│   │   ├── hero_crud.py
│   │   ├── user_crud.py
│   │   └── product_crud.py
│   │
│   ├── services/                     # 🧮 Lógica de negócio / regras de aplicação
│   │   ├── __init__.py
│   │   ├── hero_service.py
│   │   ├── user_service.py
│   │   └── product_service.py
│   │
│   ├── api/                          # 🌐 Interface com o mundo externo (rotas FastAPI)
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── hero_routes.py
│   │       ├── user_routes.py
│   │       └── product_routes.py
│   │
│   └── utils/                        # 🔧 Funções auxiliares (helpers, formatadores)
│       ├── __init__.py
│       └── email_sender.py           # Exemplo: função para envio de e-mails
│
├── tests/                            # 🧪 Testes unitários e de integração
│   ├── __init__.py
│   ├── test_hero.py
│   └── test_user.py
│
├── requirements.txt                  # 📦 Dependências do projeto
├── .env                              # 🔐 Variáveis de ambiente
├── Dockerfile                        # 🐳 Configuração Docker
└── run.py                            # 💻 Script opcional para iniciar com Uvicorn


---

## 🧠 Descrição das Camadas

| Camada | Função | Responsabilidade |
|--------|---------|------------------|
| **API (Interface)** | Controladores e endpoints. | Recebe as requisições e chama os serviços. |
| **Services (Domínio)** | Regras de negócio puras. | Define entidades e lógicas sem dependências externas. |
| **CRUD (Infraestrutura)** | Implementações técnicas. | Repositórios e acesso a dados (SQLModel, serviços externos). |
| **Core (Configuração)** | Base do sistema. | Banco, variáveis de ambiente e setup da aplicação. |
| **Models / Schemas** | Definição de dados. | Modelos do banco e validação de entrada/saída. |

Essa separação segue o princípio **“cada camada conhece apenas a inferior”**, garantindo:
- **Baixo acoplamento**  
- **Alta coesão**  
- **Facilidade para testes unitários e mocks**  

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

📦 Instalar dependências
pip install -r requirements.txt

Se ainda não tiver o arquivo requirements.txt:
pip install fastapi uvicorn sqlmodel pydantic python-dotenv
pip freeze > requirements.txt

🧰 Banco de Dados (SQLite por padrão)
from sqlmodel import create_engine, SQLModel, Session

sqlite_url = "sqlite:///./database.db"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

🏃‍♂️ Executando o Projeto
uvicorn app.main:app --reload

✅ Acesse:
📘 Swagger UI → http://127.0.0.1:8000/docs
📗 Redoc → http://127.0.0.1:8000/redoc

🧪 Exemplo de Endpoint
# app/api/v1/hero_routes.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.hero_model import Hero

router = APIRouter()

@router.get("/heroes")
def list_heroes(session: Session = Depends(get_session)):
    heroes = session.exec(select(Hero)).all()
    return heroes

🧱 Como Escalar o Projeto
Adicione novos módulos de domínio (ex: users, orders, payments) dentro da pasta domain/.
Cada módulo deve ter:
Suas entidades em entities/
Suas regras de negócio em services/
Seus repositórios em infrastructure/repositories/
Suas rotas em api/v1/
Essa abordagem permite evoluir o projeto para uma arquitetura de microsserviços, se necessário.

🧤 Contribuição
Faça um fork do repositório
Crie uma branch (git checkout -b feature/nova-feature)
Commit suas mudanças (git commit -m 'Adiciona nova feature')
Faça o push (git push origin feature/nova-feature)
Crie um Pull Request 🚀

📜 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar e modificar conforme necessário.