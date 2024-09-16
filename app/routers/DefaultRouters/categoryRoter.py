from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import verify_token
from app.controllers.DefaultControllers import categoryController as category_controller
from app.database import database
from app.schemas.DefaultSchemas import categorySchema

router = APIRouter(prefix="/crud")


@router.post("/categories/", response_model=categorySchema.CategoryCreate)
async def create_category(category: categorySchema.CategoryBase, db: AsyncSession = Depends(database.get_db)):
    return await category_controller.create_category(category=category, db=db)


@router.get("/categories/", response_model=list[categorySchema.Category])
async def read_categories(filters: str = None, skip: int = 0, limit: int = 10,
                          db: AsyncSession = Depends(database.get_db),
                          validation: str = Depends(verify_token)):
    return await category_controller.get_categories(skip=skip, limit=limit, db=db, filters=filters, model="Category")


@router.get("/categories/{category_id}", response_model=categorySchema.Category)
async def read_category(category_id: int, db: AsyncSession = Depends(database.get_db)):
    return await category_controller.get_category(category_id=category_id, db=db)


@router.put("/categories/{category_id}", response_model=categorySchema.CategoryCreate)
async def update_category(category_id: int, updated_category: categorySchema.CategoryCreate,
                          db: AsyncSession = Depends(database.get_db)):
    return await category_controller.update_category(category_id=category_id, updated_category=updated_category, db=db)


@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, db: AsyncSession = Depends(database.get_db)):
    return await category_controller.delete_category(category_id=category_id, db=db)
