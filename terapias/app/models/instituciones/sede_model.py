from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from instituciones.app.shared.db.base_class import Base
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP

class Sede(Base):
    __tablename__ = "sede"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    codigo_sede = Column(String(50), nullable=False)
    id_tipo_sede = Column(UUID(as_uuid=True), ForeignKey("tipo_sede.id", ondelete="CASCADE"), nullable=False)
    id_ciudad = Column(UUID(as_uuid=True), ForeignKey("ciudad.id", ondelete="CASCADE"), nullable=False)
    id_centro_rehabilitacion = Column(UUID(as_uuid=True), ForeignKey("centro_rehabilitacion.id", ondelete="CASCADE"), nullable=False)
    id_estado = Column(UUID(as_uuid=True), ForeignKey("estado.id", ondelete="CASCADE"), nullable=False)
    direccion = Column(String(200), nullable=False)
    telefono = Column(String(20), nullable=True)
    telefono_validado = Column(Boolean, default=False)
    correo = Column(String(100), nullable=True)
    email_validado = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relationships
    tipo_sede = relationship("TipoSede", backref="sedes")
    ciudad = relationship("Ciudad", backref="sedes") 
    centro_rehabilitacion = relationship("CentroRehabilitacion", backref="sedes")
    estado = relationship("Estado", backref="sedes")
