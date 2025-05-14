from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from instituciones.app.shared.db.base_class import Base
import uuid


class EstadoPlanRehabilitacionEjercicio(Base):
    __tablename__ = "estado_plan_rehabilitacion_ejercicio"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_codigo = Column(String(50), nullable=False, unique=True)
    id_plan_rehabilitacion = Column(UUID(as_uuid=True), ForeignKey("plan_rehabilitacion.id", ondelete="CASCADE"), nullable=False)
    id_ejercicio = Column(UUID(as_uuid=True), ForeignKey("ejercicio.id", ondelete="CASCADE"), nullable=False)
    estado = Column(String(50), nullable=False)

    plan_rehabilitacion = relationship("PlanRehabilitacion", backref="estados_ejercicios")
    ejercicio = relationship("Ejercicio", backref="planes_asociados")

