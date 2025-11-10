from sqlmodel import create_engine, SQLModel, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Criar o mecanismo de banco de dados
engine = create_engine(sqlite_url, echo=True)

# Função para criar o banco de dados e as tabelas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Função de dependência do FastAPI para abrir uma sessão de banco
def get_session():
    with Session(engine) as session:
        yield session