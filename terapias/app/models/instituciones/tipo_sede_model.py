from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from terapias.app.shared.db.base_class import Base
import uuid
from sqlalchemy.sql import func
from datetime import datetime

class TipoSede(Base):
    __tablename__ = "tipo_sede"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
