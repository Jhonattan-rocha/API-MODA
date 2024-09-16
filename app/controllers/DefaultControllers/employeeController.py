from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Employees
from app.schemas import EmployeesBase, EmployeesCreate
from app.utils import apply_filters_dynamic


async def create_employee(db: AsyncSession, employee: EmployeesBase):
    db_employee = Employees(**employee.dict())
    db.add(db_employee)
    await db.commit()
    await db.refresh(db_employee)
    return db_employee


async def get_employees(db: AsyncSession, skip: int = 0, limit: int = 10, filters: Optional[List[str]] = None,
                        model: str = ""):
    query = select(Employees)

    if filters and model:
        query = apply_filters_dynamic(query, filters, model)
    result = await db.execute(
        query
        .offset(skip)
        .limit(limit if limit > 0 else None)
    )
    return result.scalars().unique().all()


async def get_employee(db: AsyncSession, employee_id: int):
    result = await db.execute(select(Employees).where(Employees.id == employee_id))
    return result.scalars().first()


async def update_employee(db: AsyncSession, employee_id: int, updated_employee: EmployeesCreate):
    result = await db.execute(select(Employees).where(Employees.id == employee_id))
    employee = result.scalars().first()
    if employee is None:
        return None

    for key, value in updated_employee.dict().items():
        if str(value):
            setattr(employee, key, value)

    await db.commit()
    await db.refresh(employee)
    return employee


async def delete_employee(db: AsyncSession, employee_id: int):
    result = await db.execute(select(Employees).where(Employees.id == employee_id))
    employee = result.scalars().first()
    if employee is None:
        return None
    await db.delete(employee)
    await db.commit()
    return employee
