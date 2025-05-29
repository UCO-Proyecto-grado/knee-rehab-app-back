from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime
from personas.app.schemas.entidades_primarias.tipo_identificacion_schema import TipoIdentificacionOut

class UsuarioBase(BaseModel):
    id_tipo_identificacion: UUID
    identificacion: str
    nombre: str
    correo: EmailStr
    contrasena: str
    telefono: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    id_tipo_identificacion: UUID | None = None
    identificacion: str | None = None
    nombre: str | None = None
    correo: EmailStr | None = None
    contrasena: str | None = None
    telefono: str | None = None
    
    class Config:
        from_attributes = True

class UsuarioOut(UsuarioBase):
    id: UUID
    
    class Config:
        from_attributes = True