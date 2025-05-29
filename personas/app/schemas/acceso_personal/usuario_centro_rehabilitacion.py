from uuid import UUID
from pydantic import BaseModel
from personas.app.schemas.instituciones.centro_rehabilitacion_schema import CentroRehabilitacionOut
from personas.app.schemas.acceso_personal.usuario_schema import UsuarioOut

class UsuarioCentroRehabilitacionBase(BaseModel):
    id_usuario: UUID
    id_centro_rehabilitacion: UUID

class UsuarioCentroRehabilitacionCreate(UsuarioCentroRehabilitacionBase):
    pass

class UsuarioCentroRehabilitacionOut(UsuarioCentroRehabilitacionBase):
    id: UUID
    usuario: UsuarioOut
    centro_rehabilitacion: CentroRehabilitacionOut

    class Config:
        from_attributes = True
