from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.DefaultControllers import productCategoryController as product_category_controller
from app.database import database
from app.schemas.DefaultSchemas import productCategorySchema
from app.controllers import verify_token

router = APIRouter(prefix="/crud")


@router.post("/product_categories", response_model=productCategorySchema.ProductCategoryCreate)
async def create_product(product_category: productCategorySchema.ProductCategoryBase,
                         db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await product_category_controller.create_product_category(product_category=product_category, db=db)


@router.get("/product_categories", response_model=list[productCategorySchema.ProductCategory])
async def read_products(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await product_category_controller.get_product_categories(skip=skip, limit=limit, db=db)


@router.get("/product_categories/{product_category_id}", response_model=productCategorySchema.ProductCategory)
async def read_product(product_category_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await product_category_controller.get_product_category(product_category_id=product_category_id, db=db)


@router.put("/product_categories/{product_category_id}", response_model=productCategorySchema.ProductCategoryCreate)
async def update_product(product_category_id: int, updated_product_category: productCategorySchema.ProductCategoryCreate,
                         db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await product_category_controller.update_product_category(product_category_id=product_category_id,
                                                                     updated_product_category=updated_product_category,
                                                                     db=db)


@router.delete("/product_categories/{product_category_id}")
async def delete_product(product_category_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await product_category_controller.delete_product_category(product_category_id=product_category_id, db=db)
