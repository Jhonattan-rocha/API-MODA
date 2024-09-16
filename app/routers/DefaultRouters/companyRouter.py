from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import verify_token
from app.controllers.DefaultControllers import companyController as company_controller
from app.database import database
from app.schemas.DefaultSchemas import companySchema

router = APIRouter(prefix="/crud")


@router.post("/companies", response_model=companySchema.CompanyCreate)
async def create_company(company: companySchema.CompanyBase, db: AsyncSession = Depends(database.get_db)):
    return await company_controller.create_company(company=company, db=db)


@router.get("/companies", response_model=list[companySchema.Company])
async def read_company(filters: str = None, skip: int = 0, limit: int = 10,
                       db: AsyncSession = Depends(database.get_db),
                       validation: str = Depends(verify_token)):
    return await company_controller.get_companies(skip=skip, limit=limit, db=db, filters=filters, model="Company")


@router.get("/companies/{company_id}", response_model=companySchema.Company)
async def read_company(company_id: int, db: AsyncSession = Depends(database.get_db)):
    return await company_controller.get_company(company_id=company_id, db=db)


@router.put("/companies/{company_id}", response_model=companySchema.CompanyCreate)
async def update_company(company_id: int, updated_company: companySchema.CompanyCreate,
                         db: AsyncSession = Depends(database.get_db)):
    return await company_controller.update_company(company_id=company_id, updated_company=updated_company, db=db)


@router.delete("/companies/{company_id}")
async def delete_company(company_id: int, db: AsyncSession = Depends(database.get_db)):
    return await company_controller.delete_company(company_id=company_id, db=db)
