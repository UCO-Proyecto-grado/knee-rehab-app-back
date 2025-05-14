from uuid import UUID
from pydantic import BaseModel

class TipoLesionBase(BaseModel):
    abreviatura_lesion: str
    nombre: str
    descripcion: str | None = None

class TipoLesionCreate(TipoLesionBase):
    pass

class TipoLesionUpdate(TipoLesionBase):
    pass

class TipoLesionOut(TipoLesionBase):
    id: UUID

    class Config:
        from_attributes = True
