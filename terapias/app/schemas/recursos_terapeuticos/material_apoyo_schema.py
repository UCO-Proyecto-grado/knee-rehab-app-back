from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from instituciones.app.schemas.instituciones.centro_rehabilitacion_schema import CentroRehabilitacionOut

class MaterialApoyoBase(BaseModel):
    nombre: str
    recomendaciones: str
    guia_uso: str

class MaterialApoyoCreate(MaterialApoyoBase):
    pass

class MaterialApoyoUpdate(MaterialApoyoBase):
    pass

class MaterialApoyoOut(MaterialApoyoBase):
    id: UUID
    centro_rehabilitacion: CentroRehabilitacionOut
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
