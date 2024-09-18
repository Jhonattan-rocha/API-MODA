from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import ProductCategory, Category
from app.schemas import ProductCategoryBase, ProductCategoryCreate


async def create_product_category(db: AsyncSession, product_category: ProductCategoryBase):
    db_product_category = ProductCategory(**product_category.model_dump())
    db.add(db_product_category)
    await db.commit()
    await db.refresh(db_product_category)
    return db_product_category


async def get_product_categories(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(ProductCategory)
        .options(joinedload(ProductCategory.product), joinedload(ProductCategory.category).joinedload(Category.subcategories))
        .offset(skip).limit(limit)
    )
    return result.scalars().unique().all()


async def get_product_category(db: AsyncSession, product_category_id: int):
    result = await db.execute(
        select(ProductCategory)
        .options(joinedload(ProductCategory.product), joinedload(ProductCategory.category).joinedload(Category.subcategories))
        .where(ProductCategory.id == product_category_id)
    )
    return result.scalars().unique().first()


async def update_product_category(db: AsyncSession, product_category_id: int,
                                  updated_product_category: ProductCategoryCreate):
    result = await db.execute(select(ProductCategory).where(ProductCategory.id == product_category_id))
    product_category = result.scalars().first()
    if product_category is None:
        return None

    for key, value in updated_product_category.model_dump().items():
        if str(value):
            setattr(product_category, key, value)

    await db.commit()
    await db.refresh(product_category)
    return product_category


async def delete_product_category(db: AsyncSession, product_category_id: int):
    result = await db.execute(select(ProductCategory).where(ProductCategory.id == product_category_id))
    product_category = result.scalars().first()
    if product_category is None:
        return None
    await db.delete(product_category)
    await db.commit()
    return product_category
