from sqlmodel import Field, SQLModel

class HeroCreate(SQLModel):
    name: str
    secret_name: str
    age: int | None = None

class HeroRead(SQLModel):
    id: int
    name: str
    secret_name: str
    age: int | None = None