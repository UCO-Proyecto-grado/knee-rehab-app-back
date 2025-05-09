from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from shared.db.base_class import Base
import uuid

class MaterialApoyo(Base):
    __tablename__ = "material_apoyo"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_centro_rehabilitacion = Column(UUID(as_uuid=True), ForeignKey("centro_rehabilitacion.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String(100), nullable=False)
    recomendaciones = Column(String(200), nullable=True)
    guia_uso = Column(String(200), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    centro_rehabilitacion = relationship("CentroRehabilitacion", backref="material_apoyo")