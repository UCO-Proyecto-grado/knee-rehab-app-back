from pydantic import BaseModel
from uuid import UUID

class CategoriaTipoLesionBase(BaseModel):
    id_categoria: UUID
    id_lesion: UUID

class CategoriaTipoLesionCreate(CategoriaTipoLesionBase):
    pass

class CategoriaTipoLesionOut(CategoriaTipoLesionBase):
    id: UUID

    class Config:
        from_attributes = True
