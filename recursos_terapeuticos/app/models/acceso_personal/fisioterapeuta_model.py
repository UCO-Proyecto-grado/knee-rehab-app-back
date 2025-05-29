from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from recursos_terapeuticos.app.shared.db.base_class import Base
import uuid

class Fisioterapeuta(Base):
    __tablename__ = "fisioterapeuta"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_tipo_identificacion = Column(UUID(as_uuid=True), ForeignKey("tipo_identificacion.id"), nullable=False)
    identificacion = Column(String(50), nullable=False, unique=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    genero = Column(String(20), nullable=False)
    telefono = Column(String(20), nullable=True)
    telefono_validado = Column(Boolean, default=False)
    email = Column(String(100), nullable=False)
    email_validado = Column(Boolean, default=False)
    contrasena = Column(String(255), nullable=False)
    id_estado = Column(UUID(as_uuid=True), ForeignKey("estado.id"), nullable=False)

    estado = relationship("Estado")
    tipo_identificacion = relationship("TipoIdentificacion")
