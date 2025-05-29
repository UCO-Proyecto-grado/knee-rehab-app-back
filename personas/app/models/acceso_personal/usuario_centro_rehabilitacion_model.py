from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from personas.app.shared.db.base_class import Base
import uuid
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP

class UsuarioCentroRehabilitacion(Base):
    __tablename__ = "usuario_centro_rehabilitacion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)
    id_centro_rehabilitacion = Column(UUID(as_uuid=True), ForeignKey("centro_rehabilitacion.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relaciones ORM
    usuario = relationship("Usuario", backref="centros_rehabilitacion")
    centro_rehabilitacion = relationship("CentroRehabilitacion", backref="usuarios")