from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import InputOutputStock
from app.schemas import InputOutputStockBase, InputOutputStockCreate


async def create_input_output_stock(db: AsyncSession, input_output_stock: InputOutputStockBase):
    db_input_output_stock = InputOutputStock(**input_output_stock.dict())
    db.add(db_input_output_stock)
    await db.commit()
    await db.refresh(db_input_output_stock)
    return db_input_output_stock


async def get_input_output_stocks(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(InputOutputStock)
        .offset(skip).limit(limit)
    )
    return result.scalars().unique().all()


async def get_input_output_stock(db: AsyncSession, input_output_stock_id: int):
    result = await db.execute(
        select(InputOutputStock)
        .where(InputOutputStock.id == input_output_stock_id)
    )
    return result.scalars().unique().first()


async def update_input_output_stock(db: AsyncSession, input_output_stock_id: int, updated_input_output_stock: InputOutputStockCreate):
    result = await db.execute(select(InputOutputStock).where(InputOutputStock.id == input_output_stock_id))
    input_output_stock = result.scalars().first()
    if input_output_stock is None:
        return None

    for key, value in updated_input_output_stock.dict().items():
        if str(value):
            setattr(input_output_stock, key, value)

    await db.commit()
    await db.refresh(input_output_stock)
    return input_output_stock


async def delete_input_output_stock(db: AsyncSession, input_output_stock_id: int):
    result = await db.execute(select(InputOutputStock).where(InputOutputStock.id == input_output_stock_id))
    input_output_stock = result.scalars().first()
    if input_output_stock is None:
        return None
    await db.delete(input_output_stock)
    await db.commit()
    return input_output_stock
