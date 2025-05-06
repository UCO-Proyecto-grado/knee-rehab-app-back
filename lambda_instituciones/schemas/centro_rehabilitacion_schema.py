from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from lambda_entidades_primarias.schemas.tipo_identificacion_schema import TipoIdentificacionOut
class CentroRehabilitacionBase(BaseModel):
    id_tipo_identificacion: UUID
    identificacion: str
    nombre: str
    correo: EmailStr

class CentroRehabilitacionCreate(CentroRehabilitacionBase):
    pass

class CentroRehabilitacionUpdate(CentroRehabilitacionBase):
    pass

class CentroRehabilitacionOut(CentroRehabilitacionBase):
    id: UUID
    tipo_identificacion: TipoIdentificacionOut
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Habilita conversión desde SQLAlchemy
