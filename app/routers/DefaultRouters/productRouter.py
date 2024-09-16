from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers import verify_token
from app.controllers.DefaultControllers import productController as product_controller
from app.database import database
from app.schemas.DefaultSchemas import productSchema

router = APIRouter(prefix="/crud")


@router.post("/products", response_model=productSchema.ProductCreate)
async def create_product(product: productSchema.ProductBase, db: AsyncSession = Depends(database.get_db)):
    return await product_controller.create_product(product=product, db=db)


@router.get("/products", response_model=list[productSchema.Product])
async def read_products(filters: str = None, skip: int = 0, limit: int = 10,
                        db: AsyncSession = Depends(database.get_db),
                        validation: str = Depends(verify_token)):
    return await product_controller.get_products(skip=skip, limit=limit, db=db, filters=filters, model="Product")


@router.get("/products/{product_id}", response_model=productSchema.Product)
async def read_product(product_id: int, db: AsyncSession = Depends(database.get_db)):
    return await product_controller.get_product(product_id=product_id, db=db)


@router.put("/products/{product_id}", response_model=productSchema.ProductCreate)
async def update_product(product_id: int, updated_product: productSchema.ProductCreate,
                         db: AsyncSession = Depends(database.get_db)):
    return await product_controller.update_product(product_id=product_id, updated_product=updated_product, db=db)


@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(database.get_db)):
    return await product_controller.delete_product(product_id=product_id, db=db)
