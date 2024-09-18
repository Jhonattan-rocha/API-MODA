from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import SubCategory
from app.schemas import SubCategoryBase, SubCategoryCreate
from app.utils import apply_filters_dynamic


async def create_subcategory(db: AsyncSession, subcategory: SubCategoryBase):
    db_subcategory = SubCategory(**subcategory.model_dump())
    db.add(db_subcategory)
    await db.commit()
    await db.refresh(db_subcategory)
    return db_subcategory


async def get_subcategories(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                            model: str = ""):
    query = select(SubCategory)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .options(joinedload(SubCategory.category))
        .offset(skip).limit(limit)
    )
    return result.scalars().unique().all()


async def get_subcategory(db: AsyncSession, subcategory_id: int):
    result = await db.execute(
        select(SubCategory)
        .options(joinedload(SubCategory.category))
        .where(SubCategory.id == subcategory_id)
    )
    return result.scalars().unique().first()


async def update_category(db: AsyncSession, subcategory_id: int, updated_subcategory: SubCategoryCreate):
    result = await db.execute(select(SubCategory).where(SubCategory.id == subcategory_id))
    subcategory = result.scalars().first()
    if subcategory is None:
        return None

    for key, value in updated_subcategory.model_dump().items():
        if str(value):
            setattr(subcategory, key, value)

    await db.commit()
    await db.refresh(subcategory)
    return subcategory


async def delete_subcategory(db: AsyncSession, subcategory_id: int):
    result = await db.execute(select(SubCategory).where(SubCategory.id == subcategory_id))
    subcategory = result.scalars().first()
    if subcategory is None:
        return None
    await db.delete(subcategory)
    await db.commit()
    return subcategory
