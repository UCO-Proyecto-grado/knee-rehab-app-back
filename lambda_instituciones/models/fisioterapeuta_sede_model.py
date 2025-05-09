
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from shared.db.base_class import Base
import uuid

class FisioterapeutaSede(Base):
    __tablename__ = "fisioterapeuta_sede"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_fisioterapeuta = Column(UUID(as_uuid=True), ForeignKey("fisioterapeuta.id", ondelete="CASCADE"), nullable=False)
    id_sede = Column(UUID(as_uuid=True), ForeignKey("sede.id", ondelete="CASCADE"), nullable=False)

    fisioterapeuta = relationship("Fisioterapeuta", backref="sedes")
    sede = relationship("Sede", backref="fisioterapeutas")
