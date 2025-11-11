from pydantic import BaseModel

class HeroCreate(BaseModel):
    name: str
    secret_name: str
    age: int | None = None

class HeroRead(BaseModel):
    id: int
    name: str
    secret_name: str
    age: int | None = None

class HeroUpdate(BaseModel):
    name: str = None
    secret_name: str = None
    age: int | None = None