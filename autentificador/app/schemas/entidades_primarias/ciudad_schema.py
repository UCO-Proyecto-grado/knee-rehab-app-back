from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from autentificador.app.schemas.entidades_primarias.departamento_schema import DepartamentoOut

class CiudadBase(BaseModel):
    nombre: str
    id_departamento: UUID

class CiudadCreate(CiudadBase):
    pass

class CiudadUpdate(CiudadBase):
    pass

class CiudadOut(CiudadBase):
    id: UUID
    departamento: DepartamentoOut

    class Config:
        from_attributes = True
