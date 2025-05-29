from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from personas.app.shared.db.base_class import Base
import uuid
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP

class UsuarioSede(Base):
    __tablename__ = "usuario_sede"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey("usuario.id", ondelete="CASCADE"), nullable=False)
    id_sede = Column(UUID(as_uuid=True), ForeignKey("sede.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relaciones ORM
    usuario = relationship("Usuario", backref="sedes")
    sede = relationship("Sede", backref="usuarios")