from pydantic import BaseModel
from uuid import UUID
from terapias.app.schemas.acceso_personal.fisioterapeuta_schema import FisioterapeutaOut
from terapias.app.schemas.instituciones.sede_schema import SedeOut

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