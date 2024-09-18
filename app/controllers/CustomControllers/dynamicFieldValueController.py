from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import DynamicFieldToEntityValue
from app.schemas import DynamicFieldToEntityValueCreate


async def create_dynamic_field_value(db: AsyncSession, dynamic_field_value: DynamicFieldToEntityValueCreate):
    db_dynamic_field_value = DynamicFieldToEntityValue(**dynamic_field_value.model_dump())
    db.add(db_dynamic_field_value)
    await db.commit()
    await db.refresh(db_dynamic_field_value)
    return db_dynamic_field_value


async def get_dynamic_fields_values(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(DynamicFieldToEntityValue)
        .options(joinedload(DynamicFieldToEntityValue.field))
        .offset(skip).limit(limit)
    )
    return result.scalars().unique().all()


async def get_dynamic_field_value(db: AsyncSession, dynamic_field_value_id: int):
    result = await db.execute(
        select(DynamicFieldToEntityValue)
        .options(joinedload(DynamicFieldToEntityValue.field))
        .where(DynamicFieldToEntityValue.id == dynamic_field_value_id)
    )
    return result.scalars().unique().first()


async def update_dynamic_field_value(db: AsyncSession, dynamic_field_value_id: int, updated_dynamic_field_value: DynamicFieldToEntityValue):
    result = await db.execute(select(DynamicFieldToEntityValue).where(DynamicFieldToEntityValue.id == dynamic_field_value_id))
    dynamic_field_value = result.scalars().first()
    if dynamic_field_value is None:
        return None

    for key, value in updated_dynamic_field_value.model_dump().items():
        setattr(dynamic_field_value, key, value)

    await db.commit()
    await db.refresh(dynamic_field_value)
    return dynamic_field_value


async def delete_dynamic_field_value(db: AsyncSession, dynamic_field_value_id: int):
    result = await db.execute(select(DynamicFieldToEntityValue).where(DynamicFieldToEntityValue.id == dynamic_field_value_id))
    dynamic_field_value = result.scalars().first()
    if dynamic_field_value is None:
        return None
    await db.delete(dynamic_field_value)
    await db.commit()
    return dynamic_field_value
