from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.CustomControllers import dynamicEntitiesController as dynamic_entities_controller
from app.database import database
from app.schemas.CustomSchemas import dynamicEntities
from app.controllers import verify_token

router = APIRouter(prefix="/crud")


@router.post("/dynamic_entities", response_model=dynamicEntities.DynamicEntityCreate)
async def create_dynamic_entity(dynamic_entity: dynamicEntities.DynamicEntityCreate, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await dynamic_entities_controller.create_dynamic_entities(dynamic_entity=dynamic_entity, db=db)


@router.get("/dynamic_entities", response_model=list[dynamicEntities.DynamicEntity])
async def read_dynamic_entities(filters: str = None, skip: int = 0, limit: int = 10,
                                db: AsyncSession = Depends(database.get_db),
                                validation: str = Depends(verify_token)):
    return await dynamic_entities_controller.get_dynamic_entities(skip=skip, limit=limit, db=db, filters=filters, model="DynamicEntity")


@router.get("/dynamic_entities/{dynamic_entity_id}", response_model=dynamicEntities.DynamicEntity)
async def read_dynamic_entity(dynamic_entity_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await dynamic_entities_controller.get_dynamic_entity(dynamic_entity_id=dynamic_entity_id, db=db)


@router.put("/dynamic_entities/{dynamic_entity_id}", response_model=dynamicEntities.DynamicEntityCreate)
async def update_dynamic_entity(dynamic_entity_id: int, updated_dynamic_entity: dynamicEntities.DynamicEntityCreate,
                                db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await dynamic_entities_controller.update_dynamic_entity(dynamic_entity_id=dynamic_entity_id,
                                                                   updated_dynamic_entity=updated_dynamic_entity, db=db)


@router.delete("/dynamic_entities/{dynamic_entity_id}")
async def delete_dynamic_entity(dynamic_entity_id: int, db: AsyncSession = Depends(database.get_db), validation: str = Depends(verify_token)):
    return await dynamic_entities_controller.delete_dynamic_entity(dynamic_entity_id=dynamic_entity_id, db=db)
