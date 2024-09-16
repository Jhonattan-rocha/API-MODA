from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import verify_token
from app.controllers.DefaultControllers import employeeController as employee_controller
from app.database import database
from app.schemas.DefaultSchemas import employeeSchema

router = APIRouter(prefix="/crud")


@router.post("/employees", response_model=employeeSchema.EmployeesCreate)
async def create_employee(employee: employeeSchema.EmployeesBase, db: AsyncSession = Depends(database.get_db)):
    return await employee_controller.create_employee(employee=employee, db=db)


@router.get("/employees", response_model=list[employeeSchema.Employees])
async def read_employee(filters: str = None, skip: int = 0, limit: int = 10,
                        db: AsyncSession = Depends(database.get_db),
                        validation: str = Depends(verify_token)):
    return await employee_controller.get_employees(skip=skip, limit=limit, db=db, filters=filters, model="Employees")


@router.get("/employees/{employee_id}", response_model=employeeSchema.Employees)
async def read_employee(employee_id: int, db: AsyncSession = Depends(database.get_db)):
    return await employee_controller.get_employee(employee_id=employee_id, db=db)


@router.put("/employees/{employee_id}", response_model=employeeSchema.EmployeesCreate)
async def update_employee(employee_id: int, updated_employee: employeeSchema.EmployeesCreate,
                          db: AsyncSession = Depends(database.get_db)):
    return await employee_controller.update_employee(employee_id=employee_id, updated_employee=updated_employee, db=db)


@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int, db: AsyncSession = Depends(database.get_db)):
    return await employee_controller.delete_employee(employee_id=employee_id, db=db)
