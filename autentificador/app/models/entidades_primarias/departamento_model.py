from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from autentificador.app.shared.db.base_class import Base
import uuid
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    id_pais = Column(UUID(as_uuid=True), ForeignKey("pais.id"), nullable=False)

    pais = relationship("Pais", backref="departamentos")
