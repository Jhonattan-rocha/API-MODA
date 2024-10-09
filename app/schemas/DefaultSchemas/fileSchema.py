from pydantic import BaseModel

class FileBase(BaseModel):
    filename: str
    content_type: str
    description: str | None = None

class FileCreate(FileBase):
    pass

class FileResponse(FileBase):
    id: int
    file_path: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
    