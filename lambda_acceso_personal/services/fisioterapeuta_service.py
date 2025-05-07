from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_acceso_personal.models.fisioterapeuta_model import Fisioterapeuta
import uuid

def create_fisioterapeuta(db: Session, data: dict):
    existente = db.query(Fisioterapeuta).filter(Fisioterapeuta.identificacion == data["identificacion"]).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fisioterapeuta ya registrado")

    nuevo = Fisioterapeuta(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_fisioterapeutas(db: Session):
    return db.query(Fisioterapeuta).all()

def get_fisioterapeuta_by_id(db: Session, fisioterapeuta_id: uuid.UUID):
    return db.query(Fisioterapeuta).filter(Fisioterapeuta.id == fisioterapeuta_id).first()

def update_fisioterapeuta(db: Session, fisioterapeuta_id: uuid.UUID, data: dict):
    f = db.query(Fisioterapeuta).filter(Fisioterapeuta.id == fisioterapeuta_id).first()
    if not f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fisioterapeuta no encontrado")
    
    for key, value in data.items():
        setattr(f, key, value)

    db.commit()
    db.refresh(f)
    return f

def delete_fisioterapeuta(db: Session, fisioterapeuta_id: uuid.UUID):
    f = db.query(Fisioterapeuta).filter(Fisioterapeuta.id == fisioterapeuta_id).first()
    if not f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fisioterapeuta no encontrado")

    db.delete(f)
    db.commit()
    return f
