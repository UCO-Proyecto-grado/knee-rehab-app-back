from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime
from instituciones.app.schemas.entidades_primarias.ciudad_schema import CiudadOut
from instituciones.app.schemas.entidades_primarias.estado_schema import EstadoOut
from instituciones.app.schemas.instituciones.centro_rehabilitacion_schema import CentroRehabilitacionOut
from instituciones.app.schemas.instituciones.tipo_sede_schema import TipoSedeOut

class SedeBase(BaseModel):
    codigo_sede: str
    direccion: str
    telefono: Optional[str] = None
    telefono_validado: Optional[bool] = False
    correo: Optional[EmailStr] = None
    email_validado: Optional[bool] = False

class SedeCreate(SedeBase):
    id_tipo_sede: UUID
    id_ciudad: UUID
    id_centro_rehabilitacion: UUID
    id_estado: UUID
    direccion: str
    telefono: Optional[str] = None
    telefono_validado: Optional[bool] = False
    correo: Optional[EmailStr] = None
    email_validado: Optional[bool] = False

class SedeUpdate(BaseModel):
    codigo_sede: Optional[str]
    id_tipo_sede: Optional[UUID]
    id_ciudad: Optional[UUID]
    id_centro_rehabilitacion: Optional[UUID]
    id_estado: Optional[UUID]
    direccion: Optional[str]
    telefono: Optional[str]
    telefono_validado: Optional[bool]
    correo: Optional[EmailStr]
    email_validado: Optional[bool]

class SedeOut(SedeBase):
    id: UUID
    tipo_sede: TipoSedeOut
    ciudad: CiudadOut
    centro_rehabilitacion: CentroRehabilitacionOut
    estado: EstadoOut
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
