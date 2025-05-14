from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TipoIdentificacionBase(BaseModel):
    nombre: str
    codigo: str

class TipoIdentificacionCreate(TipoIdentificacionBase):
    pass

class TipoIdentificacionUpdate(TipoIdentificacionBase):
    pass

class TipoIdentificacionOut(TipoIdentificacionBase):
    id: UUID
    class Config:
        from_attributes = True
