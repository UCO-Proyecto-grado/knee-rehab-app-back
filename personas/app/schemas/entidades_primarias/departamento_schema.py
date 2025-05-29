from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from personas.app.schemas.entidades_primarias.pais_schema import PaisOut

class DepartamentoBase(BaseModel):
    nombre: str
    id_pais: UUID

class DepartamentoCreate(DepartamentoBase):
    pass

class DepartamentoUpdate(DepartamentoBase):
    pass

class DepartamentoOut(DepartamentoBase):
    id: UUID
    pais: PaisOut

    class Config:
        from_attributes = True
