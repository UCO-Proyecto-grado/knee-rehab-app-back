from uuid import UUID
from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional
from personas.app.schemas.instituciones.sede_schema import SedeOut

class PacienteBase(BaseModel):
    identificacion: str
    nombre: str
    apellido: str
    genero: str
    fecha_nacimiento: date
    telefono: str | None = None
    telefono_validado: bool = False
    email: EmailStr
    email_validado: bool = False
    contrasena: str
    direccion: str | None = None

class PacienteCreate(PacienteBase):
    id_tipo_identificacion: UUID
    id_estado: UUID
    id_ciudad: UUID
    id_sede: UUID
    

class PacienteUpdate(PacienteBase):
    id_tipo_identificacion: UUID | None = None
    id_estado: UUID | None = None
    id_ciudad: UUID | None = None
    id_sede: UUID | None = None

# New Basic Schemas for PacienteOut
class TipoIdentificacionBasicOut(BaseModel):
    nombre: str
    codigo: str

    class Config:
        from_attributes = True

class EstadoBasicOut(BaseModel):
    nombre: str

    class Config:
        from_attributes = True

class PaisBasicOut(BaseModel):
    nombre: str

    class Config:
        from_attributes = True

class DepartamentoBasicOut(BaseModel):
    nombre: str
    pais: PaisBasicOut

    class Config:
        from_attributes = True

class CiudadBasicOut(BaseModel):
    nombre: str
    departamento: DepartamentoBasicOut

    class Config:
        from_attributes = True

class PacienteOut(BaseModel):
    id: UUID
    identificacion: str
    nombre: str
    apellido: str
    genero: str
    fecha_nacimiento: date
    telefono: str | None = None
    telefono_validado: bool = False
    email: EmailStr
    email_validado: bool = False
    contrasena: str
    direccion: str | None = None
    tipo_identificacion: TipoIdentificacionBasicOut
    estado: EstadoBasicOut
    ciudad: CiudadBasicOut
    sede: SedeOut

    class Config:
        from_attributes = True