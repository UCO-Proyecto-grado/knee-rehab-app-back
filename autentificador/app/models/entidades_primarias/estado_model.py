from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from autentificador.app.shared.db.base_class import Base
import uuid

class Estado(Base):
    __tablename__ = "estado"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
