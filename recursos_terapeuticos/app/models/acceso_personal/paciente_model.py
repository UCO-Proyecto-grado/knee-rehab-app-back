from sqlalchemy import Column, String, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from recursos_terapeuticos.app.shared.db.base_class import Base
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP
from datetime import datetime
import uuid
class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id_tipo_identificacion = Column(UUID(as_uuid=True), ForeignKey("tipo_identificacion.id", ondelete="CASCADE"), nullable=False)
    identificacion = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    genero = Column(String(20))
    fecha_nacimiento = Column(Date)
    id_estado = Column(UUID(as_uuid=True), ForeignKey("estado.id", ondelete="CASCADE"), nullable=False)
    telefono = Column(String(20))
    telefono_validado = Column(Boolean, default=False)
    email = Column(String(100), nullable=False)
    email_validado = Column(Boolean, default=False)
    contrasena = Column(String(255), nullable=False)
    id_ciudad = Column(UUID(as_uuid=True), ForeignKey("ciudad.id", ondelete="CASCADE"), nullable=False)
    direccion = Column(String(200))
    id_sede = Column(UUID(as_uuid=True), ForeignKey("sede.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relaciones ORM
    sede = relationship("Sede", backref="pacientes")
    ciudad = relationship("Ciudad", backref="pacientes")
    estado = relationship("Estado", backref="pacientes")
    tipo_identificacion = relationship("TipoIdentificacion", backref="pacientes")
