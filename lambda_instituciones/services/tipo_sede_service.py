from sqlalchemy.orm import Session
from lambda_instituciones.models.tipo_sede_model import TipoSede
import uuid

def create_tipo_sede(db: Session, nombre: str):
    tipo_sede_existente = db.query(TipoSede).filter(TipoSede.nombre.ilike(nombre)).first()
    if tipo_sede_existente:
        raise ValueError("El tipo de sede ya esta registrado")
    nuevo_tipo_sede = TipoSede(nombre=nombre)
    db.add(nuevo_tipo_sede)
    db.commit()
    db.refresh(nuevo_tipo_sede)
    return nuevo_tipo_sede

def get_tipo_sedes(db: Session):
    return db.query(TipoSede).all()

def get_tipo_sede_by_id(db: Session, tipo_sede_id: uuid.UUID):
    return db.query(TipoSede).filter(TipoSede.id == tipo_sede_id).first()

def update_tipo_sede(db: Session, tipo_sede_id: uuid.UUID, nombre: str):
    tipo_sede = db.query(TipoSede).filter(TipoSede.id == tipo_sede_id).first()
    if tipo_sede:
        tipo_sede.nombre = nombre
        db.commit()
        db.refresh(tipo_sede)
    return tipo_sede

def delete_tipo_sede(db: Session, tipo_sede_id: uuid.UUID):
    tipo_sede = db.query(TipoSede).filter(TipoSede.id == tipo_sede_id).first()
    if tipo_sede:
        db.delete(tipo_sede)
        db.commit()
    return tipo_sede
