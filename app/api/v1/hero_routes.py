# app/api/v1/hero_routes.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.hero import Hero  # supondo que você tenha o modelo Hero

router = APIRouter()

@router.get("/heroes")
def list_heroes(session: Session = Depends(get_session)):
    heroes = session.exec(select(Hero)).all()
    return heroes
