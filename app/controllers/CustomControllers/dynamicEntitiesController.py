from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import DynamicEntity, DynamicFields
from app.schemas import DynamicEntityCreate
from app.utils import apply_filters_dynamic
from typing import Optional, List


async def create_dynamic_entities(db: AsyncSession, dynamic_entity: DynamicEntityCreate):
    db_dynamic_entity = DynamicEntity(**dynamic_entity.model_dump())
    db.add(db_dynamic_entity)
    await db.commit()
    await db.refresh(db_dynamic_entity)
    return db_dynamic_entity
 

async def get_dynamic_entities(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                               model: str = ""):
    query = select(DynamicEntity)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .options(joinedload(DynamicEntity.fields))
        .offset(skip).limit(limit if limit > 0 else None)
    )
    return result.scalars().unique().all()


async def get_dynamic_entity(db: AsyncSession, dynamic_entity_id: int):
    result = await db.execute(
        select(DynamicEntity)
        .options(joinedload(DynamicEntity.fields))
        .where(DynamicEntity.id == dynamic_entity_id)
    )
    return result.scalars().unique().first()


async def update_dynamic_entity(db: AsyncSession, dynamic_entity_id: int, updated_dynamic_entity: DynamicEntityCreate):
    result = await db.execute(select(DynamicEntity).where(DynamicEntity.id == dynamic_entity_id))
    dynamic_entity = result.scalars().first()
    if dynamic_entity is None:
        return None

    for key, value in updated_dynamic_entity.model_dump().items():
        setattr(dynamic_entity, key, value)

    await db.commit()
    await db.refresh(dynamic_entity)
    return dynamic_entity


async def delete_dynamic_entity(db: AsyncSession, dynamic_entity_id: int):
    result = await db.execute(select(DynamicEntity).where(DynamicEntity.id == dynamic_entity_id))
    dynamic_entity = result.scalars().first()
    if dynamic_entity is None:
        return None
    await db.delete(dynamic_entity)
    await db.commit()
    return dynamic_entity
