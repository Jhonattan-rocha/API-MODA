from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Person
from app.schemas import PersonBase, PersonCreate
from app.utils import apply_filters_dynamic


async def create_person(db: AsyncSession, person: PersonBase):
    db_person = Person(**person.model_dump())
    db.add(db_person)
    await db.commit()
    await db.refresh(db_person)
    return db_person

 
async def get_people(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                     model: str = ""):
    query = select(Person)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .offset(skip)
        .limit(limit if limit > 0 else None)
    )
    return result.scalars().all()


async def get_person(db: AsyncSession, person_id: int):
    result = await db.execute(select(Person).where(Person.id == person_id))
    return result.scalars().first()


async def update_person(db: AsyncSession, person_id: int, updated_person: PersonCreate):
    result = await db.execute(select(Person).where(Person.id == person_id))
    person = result.scalars().first()
    if person is None:
        return None

    for key, value in updated_person.model_dump().items():
        if str(value):
            setattr(person, key, value)

    await db.commit()
    await db.refresh(person)
    return person


async def delete_person(db: AsyncSession, person_id: int):
    result = await db.execute(select(Person).where(Person.id == person_id))
    person = result.scalars().first()
    if person is None:
        return None
    await db.delete(person)
    await db.commit()
    return person
