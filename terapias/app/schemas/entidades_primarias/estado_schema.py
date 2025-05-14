from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EstadoBase(BaseModel):
    nombre: str

class EstadoCreate(EstadoBase):
    pass

class EstadoUpdate(EstadoBase):
    pass

class EstadoOut(EstadoBase):
    id: UUID

    class Config:
        from_attributes = True
