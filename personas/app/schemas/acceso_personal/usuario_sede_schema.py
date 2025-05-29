from uuid import UUID
from pydantic import BaseModel
from personas.app.schemas.instituciones.sede_schema import SedeOut
from personas.app.schemas.acceso_personal.usuario_schema import UsuarioOut

class UsuarioSedeBase(BaseModel):
    id_usuario: UUID
    id_sede: UUID
    
class UsuarioSedeCreate(UsuarioSedeBase):
    pass

class UsuarioSedeOut(UsuarioSedeBase):
    id: UUID
    usuario: UsuarioOut
    sede: SedeOut
    
    class Config:
        from_attributes = True