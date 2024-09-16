from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from app.models import Company
from app.schemas import CompanyBase, CompanyCreate
from app.utils import apply_filters_dynamic


async def create_company(db: AsyncSession, company: CompanyBase):
    db_company = Company(**company.dict())
    db.add(db_company)
    await db.commit()
    await db.refresh(db_company)
    return db_company


async def get_companies(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                        model: str = ""):
    query = select(Company)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .options(joinedload(Company.employees))
        .offset(skip)
        .limit(limit if limit > 0 else None)
    )
    return result.scalars().unique().all()


async def get_company(db: AsyncSession, company_id: int):
    result = await db.execute(select(Company).where(Company.id == company_id))
    return result.scalars().first()


async def update_company(db: AsyncSession, company_id: int, updated_company: CompanyCreate):
    result = await db.execute(select(Company).where(Company.id == company_id))
    company = result.scalars().first()
    if company is None:
        return None

    for key, value in updated_company.dict().items():
        if str(value):
            setattr(company, key, value)

    await db.commit()
    await db.refresh(company)
    return company


async def delete_company(db: AsyncSession, company_id: int):
    result = await db.execute(select(Company).where(Company.id == company_id))
    company = result.scalars().first()
    if company is None:
        return None
    await db.delete(company)
    await db.commit()
    return company
