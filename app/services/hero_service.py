from fastapi import HTTPException
from sqlmodel import Session
from app.crud.hero_crud import create_hero, delete_hero, get_hero_by_id
from app.schemas.hero_schema import HeroCreate

def register_hero(session: Session, data: HeroCreate):
    if data.age and data.age < 18:
        raise ValueError("Heróis menores de idade não são permitidos.")
    return create_hero(session, data)

def delete_hero_service(session: Session, hero_id: int):
    hero = get_hero_by_id(session, hero_id) # chama a função CRUD para obter o herói
    if not hero:
        raise HTTPException(status_code=404, detail="Herói não encontrado")

    # Exemplo de regra de negócio
    if hero.age is not None and hero.age < 18:
        raise HTTPException(status_code=403, detail="Não é possível eliminar heróis menores de idade.")

    delete_hero(session, hero_id) # chama a função CRUD para eliminar o herói
    return {"message": f"Hero {hero.name} eliminado com sucesso"}