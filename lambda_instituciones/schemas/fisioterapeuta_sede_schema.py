from pydantic import BaseModel
from uuid import UUID
from lambda_acceso_personal.schemas.fisioterapeuta_schema import FisioterapeutaOut
from lambda_instituciones.schemas.sede_schema import SedeOut

class FisioterapeutaSedeBase(BaseModel):
    id_fisioterapeuta: UUID
    id_sede: UUID

class FisioterapeutaSedeCreate(FisioterapeutaSedeBase):
    pass

class FisioterapeutaSedeOut(FisioterapeutaSedeBase):
    id: UUID
    fisioterapeuta: FisioterapeutaOut
    sede: SedeOut

    class Config:
        from_attributes = True