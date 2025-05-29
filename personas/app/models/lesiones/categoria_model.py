from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from personas.app.shared.db.base_class import Base
import uuid

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
