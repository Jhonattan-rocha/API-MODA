from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.CustomControllers import dynamicFieldValueController as dynamic_fields_values_controller
from app.database import database
from app.schemas.CustomSchemas import dynamicFiledsValueSchema

router = APIRouter(prefix="/crud")


@router.post("/dynamic_fields_values", response_model=dynamicFiledsValueSchema.DynamicFieldToEntityValueCreate)
async def create_dynamic_field_value(dynamic_field_value: dynamicFiledsValueSchema.DynamicFieldToEntityValueCreate,
                                     db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_values_controller.create_dynamic_field_value(dynamic_field_value=dynamic_field_value,
                                                                             db=db)


@router.get("/dynamic_fields_values", response_model=list[dynamicFiledsValueSchema.DynamicFieldToEntityValue])
async def read_dynamic_fields(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_values_controller.get_dynamic_fields_values(skip=skip, limit=limit, db=db)


@router.get("/dynamic_fields_values/{dynamic_field_value_id}",
            response_model=dynamicFiledsValueSchema.DynamicFieldToEntityValue)
async def read_dynamic_field(dynamic_field_value_id: int, db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_values_controller.get_dynamic_field_value(dynamic_field_value_id=dynamic_field_value_id,
                                                                          db=db)


@router.put("/dynamic_fields_values/{dynamic_field_value_id}",
            response_model=dynamicFiledsValueSchema.DynamicFieldToEntityValueCreate)
async def update_dynamic_field(dynamic_field_value_id: int,
                               updated_dynamic_field_value: dynamicFiledsValueSchema.DynamicFieldToEntityValueCreate,
                               db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_values_controller.update_dynamic_field_value(
        dynamic_field_value_id=dynamic_field_value_id,
        updated_dynamic_field_value=updated_dynamic_field_value, db=db)


@router.delete("/dynamic_fields_values/{dynamic_field_value_id}")
async def delete_dynamic_field_value(dynamic_field_value_id: int, db: AsyncSession = Depends(database.get_db)):
    return await dynamic_fields_values_controller.delete_dynamic_field_value(
        dynamic_field_value_id=dynamic_field_value_id,
        db=db)
