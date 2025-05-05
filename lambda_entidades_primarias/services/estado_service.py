from sqlalchemy.orm import Session
from lambda_entidades_primarias.models.estado_model import Estado
from fastapi import HTTPException, status
import uuid

def create_estado(db: Session, nombre: str):
    existente = db.query(Estado).filter(Estado.nombre.ilike(nombre)).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El estado ya existe")

    nuevo = Estado(nombre=nombre)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_estados(db: Session):
    return db.query(Estado).all()

def get_estado_by_id(db: Session, estado_id: uuid.UUID):
    return db.query(Estado).filter(Estado.id == estado_id).first()

def update_estado(db: Session, estado_id: uuid.UUID, nombre: str):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    if not estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")

    estado.nombre = nombre
    db.commit()
    db.refresh(estado)
    return estado

def delete_estado(db: Session, estado_id: uuid.UUID):
    estado = db.query(Estado).filter(Estado.id == estado_id).first()
    if not estado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")

    db.delete(estado)
    db.commit()
    return estado
