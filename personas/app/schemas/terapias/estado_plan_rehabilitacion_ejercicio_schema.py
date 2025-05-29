from pydantic import BaseModel
from uuid import UUID


class EstadoPREBase(BaseModel):
    id_codigo: str
    id_plan_rehabilitacion: UUID
    id_ejercicio: UUID
    estado: str


class EstadoPRECreate(EstadoPREBase):
    pass


class EstadoPREUpdate(BaseModel):
    estado: str


class EstadoPREOut(EstadoPREBase):
    id: UUID

    class Config:
        from_attributes = True
