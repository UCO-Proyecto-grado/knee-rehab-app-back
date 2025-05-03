from uuid import UUID
from pydantic import BaseModel

class PaisBase(BaseModel):
    nombre: str

class PaisCreate(PaisBase):
    pass

class PaisUpdate(PaisBase):
    pass

class PaisOut(PaisBase):
    id: UUID

    class Config:
        from_attributes = True  # ✅ Requiere esto para Pydantic v2 con SQLAlchemy


