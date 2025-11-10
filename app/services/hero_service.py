from sqlmodel import Session
from app.crud.hero_crud import create_hero
from app.schemas.hero_schema import HeroCreate

def register_hero(session: Session, data: HeroCreate):
    if data.age and data.age < 18:
        raise ValueError("Heróis menores de idade não são permitidos.")
    return create_hero(session, data)
