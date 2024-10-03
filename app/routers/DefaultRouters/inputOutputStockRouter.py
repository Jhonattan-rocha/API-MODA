from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.DefaultControllers import InputOutputStockController as input_output_stock_controller
from app.database import database
from app.controllers import verify_token
from app.schemas.DefaultSchemas import inputOutputStockSchema

router = APIRouter(prefix="/crud")


@router.post("/input_output_stock/", response_model=inputOutputStockSchema.InputOutputStockBase)
async def create_category(input_output_stock: inputOutputStockSchema.InputOutputStockBase, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await input_output_stock_controller.create_input_output_stock(input_output_stock=input_output_stock, db=db)

@router.get("/input_output_stock/", response_model=list[inputOutputStockSchema.InputOutputStock])
async def read_categories(filters: str = None, skip: int = 0, limit: int = 10,
                          db: AsyncSession = Depends(database.get_db),
                          validation: str = Depends(verify_token)):
    return await input_output_stock_controller.get_input_output_stocks(skip=skip, limit=limit, db=db, filters=filters, model="InputOutputStock")


@router.get("/input_output_stock/{input_output_stock_id}", response_model=inputOutputStockSchema.InputOutputStock)
async def read_category(input_output_stock_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await input_output_stock_controller.get_input_output_stock(input_output_stock_id=input_output_stock_id, db=db)


@router.put("/input_output_stock/{input_output_stock_id}", response_model=inputOutputStockSchema.InputOutputStockCreate)
async def update_category(input_output_stock_id: int, updated_input_output_stock: inputOutputStockSchema.InputOutputStockCreate,
                          db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await input_output_stock_controller.update_input_output_stock(input_output_stock_id=input_output_stock_id,
                                                                         updated_input_output_stock=updated_input_output_stock, db=db)


@router.delete("/input_output_stock/{input_output_stock_id}")
async def delete_category(input_output_stock_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await input_output_stock_controller.delete_input_output_stock(input_output_stock_id=input_output_stock_id, db=db)
