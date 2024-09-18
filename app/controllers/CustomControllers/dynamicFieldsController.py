from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import DynamicFields
from app.schemas import DynamicFieldsCreate


async def create_dynamic_fields(db: AsyncSession, dynamic_fields: DynamicFieldsCreate):
    db_dynamic_fields = DynamicFields(**dynamic_fields.model_dump())
    db.add(db_dynamic_fields)
    await db.commit()
    await db.refresh(db_dynamic_fields)
    return db_dynamic_fields


async def get_dynamic_fields(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(DynamicFields)
        .options(joinedload(DynamicFields.value))
        .offset(skip).limit(limit)
    )
    return result.scalars().unique().all()


async def get_dynamic_field(db: AsyncSession, dynamic_field_id: int):
    result = await db.execute(
        select(DynamicFields)
        .options(joinedload(DynamicFields.value))
        .where(DynamicFields.id == dynamic_field_id)
    )
    return result.scalars().unique().first()


async def update_dynamic_field(db: AsyncSession, dynamic_field_id: int, updated_dynamic_field: DynamicFields):
    result = await db.execute(select(DynamicFields).where(DynamicFields.id == dynamic_field_id))
    dynamic_field = result.scalars().first()
    if dynamic_field is None:
        return None

    for key, value in updated_dynamic_field.model_dump().items():
        setattr(dynamic_field, key, value)

    await db.commit()
    await db.refresh(dynamic_field)
    return dynamic_field


async def delete_dynamic_field(db: AsyncSession, dynamic_field_id: int):
    result = await db.execute(select(DynamicFields).where(DynamicFields.id == dynamic_field_id))
    dynamic_field = result.scalars().first()
    if dynamic_field is None:
        return None
    await db.delete(dynamic_field)
    await db.commit()
    return dynamic_field
