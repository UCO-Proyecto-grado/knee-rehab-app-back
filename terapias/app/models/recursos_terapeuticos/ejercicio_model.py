from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from terapias.app.shared.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Ejercicio(Base):
    __tablename__ = "ejercicio"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_modulo = Column(UUID(as_uuid=True), ForeignKey("modulo.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=True)
    url_video = Column(String(300), nullable=True)
    numero_repeticiones = Column(Integer, nullable=True)
    estado_ejercicio = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    id_modulo = Column(UUID(as_uuid=True), ForeignKey("modulo.id", ondelete="CASCADE"))
    modulo = relationship("Modulo", back_populates="ejercicios")
