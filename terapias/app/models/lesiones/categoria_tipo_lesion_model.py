from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from terapias.app.shared.db.base_class import Base
import uuid

class CategoriaTipoLesion(Base):
    __tablename__ = "categoria_tipo_lesion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    id_categoria = Column(UUID(as_uuid=True), ForeignKey("categoria.id", ondelete="CASCADE"), nullable=False)
    id_lesion = Column(UUID(as_uuid=True), ForeignKey("tipo_lesion.id", ondelete="CASCADE"), nullable=False)

    categoria = relationship("Categoria", backref="tipos_lesion_asociados")
    tipo_lesion = relationship("TipoLesion", backref="categorias_asociadas")
