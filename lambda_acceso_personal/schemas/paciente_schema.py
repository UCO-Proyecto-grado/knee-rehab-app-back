from uuid import UUID
from datetime import date
from pydantic import BaseModel, EmailStr

class PacienteBase(BaseModel):
    id_tipo_identificacion: UUID
    identificacion: str
    nombre: str
    apellido: str
    genero: str
    fecha_nacimiento: date
    id_estado: UUID
    telefono: str | None = None
    telefono_validado: bool = False
    email: EmailStr
    email_validado: bool = False
    contrasena: str
    id_ciudad: UUID
    direccion: str | None = None

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class PacienteOut(PacienteBase):
    id: UUID

    class Config:
        from_attributes = True
