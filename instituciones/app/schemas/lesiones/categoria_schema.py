from uuid import UUID
from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    pass

class CategoriaOut(CategoriaBase):
    id: UUID

    class Config:
        from_attributes = True
