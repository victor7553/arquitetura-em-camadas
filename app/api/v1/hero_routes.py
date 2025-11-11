# app/api/v1/hero_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.crud.hero_crud import create_hero, delete_hero, get_hero_by_id, update_hero
from app.schemas.hero_schema import HeroCreate, HeroUpdate
from app.core.database import get_session
from app.models.hero import Hero
from app.services.hero_service import delete_hero_service  # supondo que você tenha o modelo Hero

router = APIRouter()

@router.get("/heroes")
def list_heroes(session: Session = Depends(get_session)):
    heroes = session.exec(select(Hero)).all()
    return heroes

@router.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = get_hero_by_id(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@router.post("/create_hero", response_model=Hero)
def create_hero_v2(hero: HeroCreate, session: Session = Depends(get_session)):
    hero_db = Hero(**hero.model_dump())  # conversão
    db_record = create_hero(session, hero_db)
    return db_record

@router.put("heroe_update/{hero_id}", response_model=Hero)
def heroe_update(hero_id: int, hero: HeroUpdate, session: Session = Depends(get_session)):
    db_record = update_hero(session, hero_id, hero)
    if not db_record:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_record

@router.delete("/heroes/{hero_id}", response_model=Hero)
def hero_delete(hero_id: int, session: Session = Depends(get_session)):
    db_record = delete_hero(session, hero_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_record

#  modo com serviço e regras de negócio
# Lida com requisições HTTP e respostas
@router.delete("/heroes_v2/{hero_id}")
def delete_hero_v2(hero_id: int, session: Session = Depends(get_session)):
    return delete_hero_service(session, hero_id)