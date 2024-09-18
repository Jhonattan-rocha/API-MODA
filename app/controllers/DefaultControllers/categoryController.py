from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import Category
from app.schemas import CategoryBase, CategoryCreate
from app.utils import apply_filters_dynamic


async def create_category(db: AsyncSession, category: CategoryBase):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                         model: str = ""):
    query = select(Category)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .options(joinedload(Category.subcategories))
        .offset(skip).limit(limit if limit > 0 else None)
    )
    return result.scalars().unique().all()


async def get_category(db: AsyncSession, category_id: int):
    result = await db.execute(
        select(Category)
        .options(joinedload(Category.subcategories))
        .where(Category.id == category_id)
    )
    return result.scalars().unique().first()


async def update_category(db: AsyncSession, category_id: int, updated_category: CategoryCreate):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalars().first()
    if category is None:
        return None

    for key, value in updated_category.model_dump().items():
        if str(value):
            setattr(category, key, value)

    await db.commit()
    await db.refresh(category)
    return category


async def delete_category(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalars().first()
    if category is None:
        return None
    await db.delete(category)
    await db.commit()
    return category
