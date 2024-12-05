from typing import Optional, List

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models import Logger, User, UserProfile
from app.schemas import LoggerBase, LoggerCreate
from app.utils import apply_filters_dynamic

async def create_log(db: AsyncSession, log: LoggerBase):
    db_log = Logger(**log.model_dump())
    db.add(db_log)
    await db.commit()
    await db.refresh(db_log)
    return db_log


async def get_logs(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                   model: str = ""):
    query = select(Logger)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .options(joinedload(Logger.user).joinedload(User.profile).joinedload(UserProfile.permissions))
        .offset(skip)
        .limit(limit if limit > 0 else None)
    )
    return result.scalars().unique().all()

async def delete_log(db: AsyncSession, log_id: int):
    result = await db.execute(select(Logger).where(Logger.id == log_id))
    log = result.scalars().first()
    if log is None:
        return None
    await db.delete(log)
    await db.commit()
    return log
