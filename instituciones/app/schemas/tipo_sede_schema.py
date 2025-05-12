from uuid import UUID
from pydantic import BaseModel

class TipoSedeBase(BaseModel):
    nombre: str

class TipoSedeCreate(TipoSedeBase):
    pass

class TipoSedeUpdate(TipoSedeBase):
    pass

class TipoSedeOut(TipoSedeBase):
    id: UUID

    class Config:
        from_attributes = True