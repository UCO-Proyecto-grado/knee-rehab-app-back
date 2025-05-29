from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from instituciones.app.schemas.instituciones.centro_rehabilitacion_schema import CentroRehabilitacionOut
class ModuloBase(BaseModel):
    nombre: str
    descripcion: str
    id_centro_rehabilitacion: UUID

class ModuloCreate(ModuloBase):
    pass

class ModuloUpdate(ModuloBase):
    pass

class ModuloOut(ModuloBase):
    id: UUID
    centro_rehabilitacion: CentroRehabilitacionOut
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True