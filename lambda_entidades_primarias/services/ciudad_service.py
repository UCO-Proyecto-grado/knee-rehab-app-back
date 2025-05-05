from sqlalchemy.orm import Session, joinedload
from lambda_entidades_primarias.models.ciudad_model import Ciudad
from lambda_entidades_primarias.models.departamento_model import Departamento
from fastapi import HTTPException, status
import uuid

def create_ciudad(db: Session, nombre: str, id_departamento: uuid.UUID):
    dep = db.query(Departamento).filter(Departamento.id == id_departamento).first()
    if not dep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")

    existente = db.query(Ciudad).filter(
        Ciudad.nombre.ilike(nombre),
        Ciudad.id_departamento == id_departamento
    ).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La ciudad ya existe en ese departamento")

    nueva = Ciudad(nombre=nombre, id_departamento=id_departamento)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def get_ciudades(db: Session):
    return db.query(Ciudad).options(joinedload(Ciudad.departamento)).all()

def get_ciudad_by_id(db: Session, ciudad_id: uuid.UUID):
    return db.query(Ciudad).options(joinedload(Ciudad.departamento)).filter(Ciudad.id == ciudad_id).first()

def update_ciudad(db: Session, ciudad_id: uuid.UUID, nombre: str, id_departamento: uuid.UUID):
    ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
    if not ciudad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")
    
    ciudad.nombre = nombre
    ciudad.id_departamento = id_departamento
    db.commit()
    db.refresh(ciudad)
    return ciudad

def delete_ciudad(db: Session, ciudad_id: uuid.UUID):
    ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
    if not ciudad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")
    
    db.delete(ciudad)
    db.commit()
    return ciudad
