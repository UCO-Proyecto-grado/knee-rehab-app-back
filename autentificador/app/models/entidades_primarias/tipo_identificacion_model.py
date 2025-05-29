from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from autentificador.app.shared.db.base_class import Base
import uuid

class TipoIdentificacion(Base):
    __tablename__ = "tipo_identificacion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(10), nullable=False)
