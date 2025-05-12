from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class PaisBase(BaseModel):
    nombre: str

class PaisCreate(PaisBase):
    pass

class PaisUpdate(PaisBase):
    pass

class PaisOut(PaisBase):
    id: UUID

    class Config:
        from_attributes = True


class DepartamentoBase(BaseModel):
    nombre: str
    id_pais: UUID

class DepartamentoCreate(DepartamentoBase):
    pass

class DepartamentoUpdate(DepartamentoBase):
    pass

class DepartamentoOut(DepartamentoBase):
    id: UUID
    pais: PaisOut

    class Config:
        from_attributes = True


class CiudadBase(BaseModel):
    nombre: str
    id_departamento: UUID

class CiudadCreate(CiudadBase):
    pass

class CiudadUpdate(CiudadBase):
    pass

class CiudadOut(CiudadBase):
    id: UUID
    departamento: DepartamentoOut

    class Config:
        from_attributes = True

class EstadoBase(BaseModel):
    nombre: str

class EstadoCreate(EstadoBase):
    pass

class EstadoUpdate(EstadoBase):
    pass

class EstadoOut(EstadoBase):
    id: UUID

    class Config:
        from_attributes = True


class TipoIdentificacionBase(BaseModel):
    nombre: str
    codigo: str

class TipoIdentificacionCreate(TipoIdentificacionBase):
    pass

class TipoIdentificacionUpdate(TipoIdentificacionBase):
    pass

class TipoIdentificacionOut(TipoIdentificacionBase):
    id: UUID
    class Config:
        from_attributes = True
