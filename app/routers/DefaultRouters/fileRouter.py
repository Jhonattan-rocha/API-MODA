from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.controllers.DefaultControllers import fileController as file_controller
from app.database import database
from app.controllers import verify_token
from app.schemas.DefaultSchemas import fileSchema
import shutil
import os

router = APIRouter(prefix="/crud")

# Upload de Arquivos
@router.post("/files/", response_model=fileSchema.FileResponse)
async def create_file(
    file: UploadFile = File(...), description: str = "", db: AsyncSession = Depends(database.get_db), validation: int = Depends(verify_token)
):
    file_location = f"files/{file.filename}"  # Define o caminho para salvar o arquivo

    # Salvar arquivo no sistema de arquivos
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Criar um registro no banco de dados
    db_file = await file_controller.create_file(
        db=db,
        file=fileSchema.FileCreate(
            filename=file.filename,
            content_type=file.content_type,
            description=description,
        ),
        file_path=file_location,
    )
    return db_file

@router.get("/files/download/{file_id}", response_class=FileResponse)
async def download_file(file_id: int, db: AsyncSession = Depends(database.get_db)):
    db_file = await file_controller.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")

    # Verificar se o arquivo existe no caminho especificado
    if not os.path.exists(db_file.file_path):
        raise HTTPException(status_code=404, detail="File not found on server")

    # Retornar o arquivo para download
    return FileResponse(path=db_file.file_path, filename=db_file.filename, media_type=db_file.content_type)


@router.get("/files/", response_model=list[fileSchema.FileResponse])
async def read_files(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db), validation: int = Depends(verify_token)):
    files = await file_controller.get_files(db=db, skip=skip, limit=limit)
    return files

@router.get("/files/{file_id}", response_model=fileSchema.FileResponse)
async def read_file(file_id: int, db: AsyncSession = Depends(database.get_db), validation: int = Depends(verify_token)):
    db_file = await file_controller.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file

@router.delete("/files/{file_id}", response_model=bool)
async def delete_file(file_id: int, db: AsyncSession = Depends(database.get_db), validation: int = Depends(verify_token)):
    result = await file_controller.delete_file(db=db, file_id=file_id)
    if not result:
        raise HTTPException(status_code=404, detail="File not found")
    return True