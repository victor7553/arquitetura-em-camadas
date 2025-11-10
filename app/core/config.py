# camada de infraestrutura e configuração
from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "FastAPI SQLModel Example"
    sqlite_file_name: str = "database.db"
    sqlite_url: str = f"sqlite:///{sqlite_file_name}"

settings = Settings()