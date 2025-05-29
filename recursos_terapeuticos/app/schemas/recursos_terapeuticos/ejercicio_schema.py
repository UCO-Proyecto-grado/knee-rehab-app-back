from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from recursos_terapeuticos.app.schemas.recursos_terapeuticos.modulo_schema import ModuloOut


class EjercicioBase(BaseModel):
    nombre: str
    id_modulo: UUID
    descripcion: str
    url_video: str
    numero_repeticiones: int
    estado_ejercicio: str

class EjercicioCreate(EjercicioBase):
    pass

class EjercicioUpdate(EjercicioBase):
    pass

class EjercicioOut(EjercicioBase):
    id: UUID
    modulo: ModuloOut
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True