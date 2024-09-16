from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.CustomControllers import dynamicFieldsController as dynamic_fields_controller
from app.database import database
from app.schemas.CustomSchemas import dynamicFields

router = APIRouter(prefix="/crud")


@router.post("/dynamic_fields", response_model=dynamicFields.DynamicFieldsCreate)
async def create_dynamic_field(dynamic_fields: dynamicFields.DynamicFieldsCreate,
                               db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_controller.create_dynamic_fields(dynamic_fields=dynamic_fields, db=db)


@router.get("/dynamic_fields", response_model=list[dynamicFields.DynamicFields])
async def read_dynamic_fields(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_controller.get_dynamic_fields(skip=skip, limit=limit, db=db)


@router.get("/dynamic_fields/{dynamic_field_id}", response_model=dynamicFields.DynamicFields)
async def read_dynamic_field(dynamic_field_id: int, db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_controller.get_dynamic_field(dynamic_field_id=dynamic_field_id, db=db)


@router.put("/dynamic_fields/{dynamic_field_id}", response_model=dynamicFields.DynamicFields)
async def update_dynamic_field(dynamic_field_id: int, updated_dynamic_field: dynamicFields.DynamicFields,
                               db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_controller.update_dynamic_field(dynamic_field_id=dynamic_field_id,
                                                                updated_dynamic_field=updated_dynamic_field, db=db)


@router.delete("/dynamic_fields/{dynamic_field_id}")
async def delete_dynamic_field(dynamic_field_id: int, db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_controller.delete_dynamic_field(dynamic_field_id=dynamic_field_id, db=db)
