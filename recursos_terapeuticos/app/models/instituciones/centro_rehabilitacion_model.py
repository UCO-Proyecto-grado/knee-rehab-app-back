from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from recursos_terapeuticos.app.shared.db.base_class import Base
import uuid

class CentroRehabilitacion(Base):
    __tablename__ = "centro_rehabilitacion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_tipo_identificacion = Column(UUID(as_uuid=True), ForeignKey("tipo_identificacion.id", ondelete="CASCADE"), nullable=False)
    identificacion = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    tipo_identificacion = relationship("TipoIdentificacion", backref="centros_rehabilitacion")