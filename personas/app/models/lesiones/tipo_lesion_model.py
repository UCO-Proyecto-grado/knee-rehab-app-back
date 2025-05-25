from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from personas.app.shared.db.base_class import Base
import uuid

class TipoLesion(Base):
    __tablename__ = "tipo_lesion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    abreviatura_lesion = Column(String(20), nullable=False, unique=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
