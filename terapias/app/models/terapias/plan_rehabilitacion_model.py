from sqlalchemy import Column, String, Text, Boolean, Date, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from terapias.app.shared.db.base_class import Base
import uuid


class PlanRehabilitacion(Base):
    __tablename__ = "plan_rehabilitacion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    codigo_plan_rehabilitacion = Column(String(50), nullable=False, unique=True)
    nombre = Column(String(100), nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    finalizado = Column(Boolean, default=False)
    porcentaje_finalizacion = Column(Numeric(5, 2), default=0.00)

    id_fisioterapeuta_sede = Column(UUID(as_uuid=True), ForeignKey("fisioterapeuta_sede.id"), nullable=False)
    id_estado = Column(UUID(as_uuid=True), ForeignKey("estado.id"), nullable=False)
    id_paciente_categoria_tipo_lesion = Column(UUID(as_uuid=True), ForeignKey("paciente_categoria_tipo_lesion.id"), nullable=False)

    observaciones = Column(Text, nullable=True)

    # Relaciones
    # fisioterapeuta_sede = relationship("FisioterapeutaSede", backref="planes_rehabilitacion")
    estado = relationship("Estado", backref="planes_rehabilitacion")
    paciente_categoria_tipo_lesion = relationship("PacienteCategoriaTipoLesion", backref="planes_rehabilitacion")
