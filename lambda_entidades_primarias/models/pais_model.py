from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from shared.db.base_class import Base
import uuid

class Pais(Base):
    __tablename__ = "pais"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
