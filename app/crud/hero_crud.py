from sqlmodel import Session, select
from app.models.hero import Hero

def get_heroes(session: Session):
    return session.exec(select(Hero)).all()

def create_hero(session: Session, hero: Hero):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero