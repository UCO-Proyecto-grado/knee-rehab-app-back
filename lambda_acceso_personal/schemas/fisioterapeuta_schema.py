from uuid import UUID
from pydantic import BaseModel, EmailStr

class FisioterapeutaBase(BaseModel):
    id_tipo_identificacion: UUID
    identificacion: str
    nombre: str
    apellido: str
    genero: str
    telefono: str | None = None
    telefono_validado: bool = False
    email: EmailStr
    email_validado: bool = False
    contrasena: str
    id_estado: UUID

class FisioterapeutaCreate(FisioterapeutaBase):
    pass

class FisioterapeutaUpdate(FisioterapeutaBase):
    pass

class FisioterapeutaOut(FisioterapeutaBase):
    id: UUID

    class Config:
        from_attributes = True
