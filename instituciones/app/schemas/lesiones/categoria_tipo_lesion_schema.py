from pydantic import BaseModel
from uuid import UUID
from instituciones.app.schemas.lesiones.categoria_schema import CategoriaOut
from instituciones.app.schemas.lesiones.tipo_lesion_schema import TipoLesionOut

class CategoriaTipoLesionBase(BaseModel):
    id_categoria: UUID
    id_lesion: UUID

class CategoriaTipoLesionCreate(CategoriaTipoLesionBase):
    pass

class CategoriaTipoLesionOut(CategoriaTipoLesionBase):
    id: UUID
    categoria: CategoriaOut
    tipo_lesion: TipoLesionOut

    class Config:
        from_attributes = True
