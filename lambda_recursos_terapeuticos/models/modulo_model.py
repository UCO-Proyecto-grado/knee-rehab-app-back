from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from shared.db.base_class import Base
import uuid

class Modulo(Base):
    __tablename__ = "modulo"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_centro_rehabilitacion = Column(UUID(as_uuid=True), ForeignKey("centro_rehabilitacion.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    centro_rehabilitacion = relationship("CentroRehabilitacion", backref="modulos")
    ejercicios = relationship("Ejercicio", back_populates="modulo", cascade="all, delete-orphan")
    