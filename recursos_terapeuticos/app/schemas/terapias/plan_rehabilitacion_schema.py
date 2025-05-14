from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional
from decimal import Decimal


class PlanRehabilitacionBase(BaseModel):
    codigo_plan_rehabilitacion: str
    nombre: str
    fecha_creacion: date
    finalizado: Optional[bool] = False
    porcentaje_finalizacion: Optional[Decimal] = 0.00
    observaciones: Optional[str] = None
    id_fisioterapeuta_sede: UUID
    id_estado: UUID
    id_paciente_categoria_tipo_lesion: UUID


class PlanRehabilitacionCreate(PlanRehabilitacionBase):
    pass


class PlanRehabilitacionUpdate(BaseModel):
    nombre: Optional[str]
    finalizado: Optional[bool]
    porcentaje_finalizacion: Optional[Decimal]
    observaciones: Optional[str]
    id_estado: Optional[UUID]


class PlanRehabilitacionOut(PlanRehabilitacionBase):
    id: UUID

    class Config:
        from_attributes = True
