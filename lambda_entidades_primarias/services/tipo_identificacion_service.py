from sqlalchemy.orm import Session
from lambda_entidades_primarias.models.tipo_identificacion_model import TipoIdentificacion
from fastapi import HTTPException, status
import uuid

def create_tipo_identificacion(db: Session, nombre: str, codigo: str):
    existente = db.query(TipoIdentificacion).filter(
        TipoIdentificacion.nombre.ilike(nombre)
    ).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tipo de identificación ya existe")

    nuevo = TipoIdentificacion(nombre=nombre, codigo=codigo)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_tipos_identificacion(db: Session):
    return db.query(TipoIdentificacion).all()

def get_tipo_identificacion_by_id(db: Session, tipo_id: uuid.UUID):
    return db.query(TipoIdentificacion).filter(TipoIdentificacion.id == tipo_id).first()

def update_tipo_identificacion(db: Session, tipo_id: uuid.UUID, nombre: str, codigo: str):
    tipo = db.query(TipoIdentificacion).filter(TipoIdentificacion.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo no encontrado")
    
    tipo.nombre = nombre
    tipo.codigo = codigo
    db.commit()
    db.refresh(tipo)
    return tipo

def delete_tipo_identificacion(db: Session, tipo_id: uuid.UUID):
    tipo = db.query(TipoIdentificacion).filter(TipoIdentificacion.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo no encontrado")
    
    db.delete(tipo)
    db.commit()
    return tipo
