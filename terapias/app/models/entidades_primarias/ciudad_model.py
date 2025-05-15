from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from terapias.app.shared.db.base_class import Base
import uuid

class Ciudad(Base):
    __tablename__ = "ciudad"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    id_departamento = Column(UUID(as_uuid=True), ForeignKey("departamento.id"), nullable=False)

    departamento = relationship("Departamento", backref="ciudades")
