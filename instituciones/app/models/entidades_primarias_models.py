from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from instituciones.app.shared.db.base_class import Base
import uuid

class Pais(Base):
    __tablename__ = "pais"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from instituciones.app.shared.db.base_class import Base
import uuid
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class Departamento(Base):
    __tablename__ = "departamento"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    id_pais = Column(UUID(as_uuid=True), ForeignKey("pais.id"), nullable=False)

    pais = relationship("Pais", backref="departamentos")

class Ciudad(Base):
    __tablename__ = "ciudad"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    id_departamento = Column(UUID(as_uuid=True), ForeignKey("departamento.id"), nullable=False)

    departamento = relationship("Departamento", backref="ciudades")

class Estado(Base):
    __tablename__ = "estado"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)

class TipoIdentificacion(Base):
    __tablename__ = "tipo_identificacion"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(10), nullable=False)
