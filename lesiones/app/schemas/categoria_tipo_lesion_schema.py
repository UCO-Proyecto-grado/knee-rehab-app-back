from pydantic import BaseModel
from uuid import UUID
from lesiones.app.schemas.categoria_schema import CategoriaOut
from lesiones.app.schemas.tipo_lesion_schema import TipoLesionOut

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
