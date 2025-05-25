from sqlalchemy import Column, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from personas.app.shared.db.base_class import Base
import uuid
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP
class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_tipo_identificacion = Column(UUID(as_uuid=True), ForeignKey("tipo_identificacion.id", ondelete="CASCADE"), nullable=False)
    identificacion = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    contrasena = Column(String(255), nullable=False)
    telefono = Column(String(20))

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relaciones ORM
    tipo_identificacion = relationship("TipoIdentificacion", backref="usuarios")
