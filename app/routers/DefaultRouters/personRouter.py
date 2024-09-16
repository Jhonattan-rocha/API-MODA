from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.DefaultControllers import personController as person_controller
from app.database import database
from app.schemas.DefaultSchemas import personSchema

router = APIRouter(prefix="/crud")


@router.post("/people", response_model=personSchema.PersonCreate)
async def create_people(person: personSchema.PersonBase, db: AsyncSession = Depends(database.get_db)):
    return await person_controller.create_person(person=person, db=db)


@router.get("/people", response_model=list[personSchema.Person])
async def read_people(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    return await person_controller.get_people(skip=skip, limit=limit, db=db)


@router.get("/people/{person_id}", response_model=personSchema.Person)
async def read_people(person_id: int, db: AsyncSession = Depends(database.get_db)):
    return await person_controller.get_person(person_id=person_id, db=db)


@router.put("/people/{person_id}", response_model=personSchema.PersonCreate)
async def update_people(person_id: int, updated_person: personSchema.PersonCreate,
                        db: AsyncSession = Depends(database.get_db)):
    return await person_controller.update_person(person_id=person_id, updated_person=updated_person, db=db)


@router.delete("/people/{person_id}")
async def delete_people(person_id: int, db: AsyncSession = Depends(database.get_db)):
    return await person_controller.delete_person(person_id=person_id, db=db)
