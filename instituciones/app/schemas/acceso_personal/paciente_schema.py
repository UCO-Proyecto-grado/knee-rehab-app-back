from uuid import UUID
from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from instituciones.app.schemas.instituciones.sede_schema import SedeOut
from instituciones.app.schemas.entidades_primarias.ciudad_schema import CiudadOut
from instituciones.app.schemas.entidades_primarias.estado_schema import EstadoOut
from instituciones.app.schemas.entidades_primarias.tipo_identificacion_schema import TipoIdentificacionOut

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
    pass

class PacienteOut(BaseModel):
    id: UUID
    tipo_identificacion: TipoIdentificacionOut
    estado: EstadoOut
    ciudad: CiudadOut
    sede: SedeOut

    class Config:
        from_attributes = True