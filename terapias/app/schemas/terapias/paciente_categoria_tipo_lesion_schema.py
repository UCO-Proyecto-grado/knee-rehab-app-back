from pydantic import BaseModel
from uuid import UUID


class PacienteCategoriaTipoLesionBase(BaseModel):
    id_paciente: UUID
    id_categoria_tipo_lesion: UUID


class PacienteCategoriaTipoLesionCreate(PacienteCategoriaTipoLesionBase):
    pass


class PacienteCategoriaTipoLesionOut(PacienteCategoriaTipoLesionBase):
    id: UUID

    class Config:
        from_attributes = True
