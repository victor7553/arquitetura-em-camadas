from sqlmodel import Session, select
from app.models.hero import Hero

def get_heroes(session: Session):
    return session.exec(select(Hero)).all()

def get_hero_by_id(session: Session, hero_id: int) -> Hero | None:
    return session.exec(select(Hero).where(Hero.id == hero_id)).first()

def create_hero(session: Session, hero: Hero):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

def update_hero(session: Session, hero_id: int, hero: Hero):
    db_hero = get_hero_by_id(session, hero_id)
    if not db_hero:
        return None

    hero_data = hero.model_dump(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_hero, key, value)

    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

def delete_hero(session: Session, hero_id: int):
    hero = get_hero_by_id(session, hero_id)
    if not hero:
        return None

    session.delete(hero)
    session.commit()
    return hero