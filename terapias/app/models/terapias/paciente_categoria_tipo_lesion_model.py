from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from terapias.app.shared.db.base_class import Base
import uuid


class PacienteCategoriaTipoLesion(Base):
    __tablename__ = "paciente_categoria_tipo_lesion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_paciente = Column(UUID(as_uuid=True), ForeignKey("paciente.id", ondelete="CASCADE"), nullable=False)
    id_categoria_tipo_lesion = Column(UUID(as_uuid=True), ForeignKey("categoria_tipo_lesion.id", ondelete="CASCADE"), nullable=False)

    paciente = relationship("Paciente", backref="relaciones_lesiones")
    categoria_tipo_lesion = relationship("CategoriaTipoLesion", backref="pacientes_asociados")
