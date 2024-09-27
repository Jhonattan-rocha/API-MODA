from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import verify_token
from app.controllers.DefaultControllers import subCategoryController as sub_category_controller
from app.database import database
from app.schemas.DefaultSchemas import subCategorySchema

router = APIRouter(prefix="/crud")


@router.post("/subcategories/", response_model=subCategorySchema.SubCategoryCreate)
async def create_subcategory(subcategory: subCategorySchema.SubCategoryBase,
                             db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await sub_category_controller.create_subcategory(subcategory=subcategory, db=db)


@router.get("/subcategories/", response_model=list[subCategorySchema.SubCategory])
async def read_subcategories(filters: str = None, skip: int = 0, limit: int = 10,
                             db: AsyncSession = Depends(database.get_db),
                             validation: str = Depends(verify_token)):
    return await sub_category_controller.get_subcategories(skip=skip, limit=limit, db=db, filters=filters,
                                                           model="SubCategory")


@router.get("/subcategories/{subcategory_id}", response_model=subCategorySchema.SubCategory)
async def read_subcategory(subcategory_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await sub_category_controller.get_subcategory(subcategory_id=subcategory_id, db=db)


@router.put("/subcategories/{subcategory_id}", response_model=subCategorySchema.SubCategoryCreate)
async def update_subcategory(subcategory_id: int, updated_subcategory: subCategorySchema.SubCategoryCreate,
                             db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await sub_category_controller.update_category(subcategory_id=subcategory_id,
                                                         updated_subcategory=updated_subcategory, db=db)


@router.delete("/subcategories/{subcategory_id}")
async def delete_subcategory(subcategory_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await sub_category_controller.delete_subcategory(subcategory_id=subcategory_id, db=db)
