from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import Product
from app.schemas import ProductBase, ProductCreate
from app.utils import apply_filters_dynamic


async def create_product(db: AsyncSession, product: ProductBase):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                       model: str = ""):

    query = select(Product)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .offset(skip).limit(limit)
    )
    return result.scalars().unique().all()


async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(
        select(Product)
        .where(Product.id == product_id)
    )
    return result.scalars().unique().first()


async def update_product(db: AsyncSession, product_id: int, updated_product: ProductCreate):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalars().first()
    if product is None:
        return None

    for key, value in updated_product.dict().items():
        if str(value):
            setattr(product, key, value)

    await db.commit()
    await db.refresh(product)
    return product


async def delete_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalars().first()
    if product is None:
        return None
    await db.delete(product)
    await db.commit()
    return product
