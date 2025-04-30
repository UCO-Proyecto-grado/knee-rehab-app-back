from sqlalchemy.orm import Session
from lambda_entidades_primarias. models.pais_model import Pais
import uuid

def create_pais(db: Session, nombre: str):
    pais_existente = db.query(Pais).filter(Pais.nombre.ilike(nombre)).first()
    if pais_existente:
        raise ValueError("El país ya esta registrado")
    nuevo_pais = Pais(nombre=nombre)
    db.add(nuevo_pais)
    db.commit()
    db.refresh(nuevo_pais)
    return nuevo_pais

def get_paises(db: Session):
    return db.query(Pais).all()

def get_pais_by_id(db: Session, pais_id: uuid.UUID):
    return db.query(Pais).filter(Pais.id == pais_id).first()

def update_pais(db: Session, pais_id: uuid.UUID, nombre: str):
    pais = db.query(Pais).filter(Pais.id == pais_id).first()
    if pais:
        pais.nombre = nombre
        db.commit()
        db.refresh(pais)
    return pais

def delete_pais(db: Session, pais_id: uuid.UUID):
    pais = db.query(Pais).filter(Pais.id == pais_id).first()
    if pais:
        db.delete(pais)
        db.commit()
    return pais
