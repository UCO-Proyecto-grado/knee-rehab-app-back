from sqlalchemy.orm import Session, joinedload
from lambda_entidades_primarias.models.departamento_model import Departamento
from lambda_entidades_primarias.models.pais_model import Pais
import uuid
from fastapi import HTTPException, status

def create_departamento(db: Session, nombre: str, id_pais: uuid.UUID):
    pais = db.query(Pais).filter(Pais.id == id_pais).first()
    if not pais:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="País no encontrado")
    
    existente = db.query(Departamento).filter(
        Departamento.nombre.ilike(nombre),
        Departamento.id_pais == id_pais
    ).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El departamento ya está registrado para este país")
    
    nuevo = Departamento(nombre=nombre, id_pais=id_pais)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_departamentos(db: Session):
    return db.query(Departamento).options(joinedload(Departamento.pais)).all()

def get_departamento_by_id(db: Session, departamento_id: uuid.UUID):
    return db.query(Departamento).options(joinedload(Departamento.pais)).filter(Departamento.id == departamento_id).first()

def update_departamento(db: Session, departamento_id: uuid.UUID, nombre: str, id_pais: uuid.UUID):
    departamento = db.query(Departamento).filter(Departamento.id == departamento_id).first()
    if not departamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")

    departamento.nombre = nombre
    departamento.id_pais = id_pais
    db.commit()
    db.refresh(departamento)
    return departamento

def delete_departamento(db: Session, departamento_id: uuid.UUID):
    departamento = db.query(Departamento).filter(Departamento.id == departamento_id).first()
    if not departamento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")
    
    db.delete(departamento)
    db.commit()
    return departamento
