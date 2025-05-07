from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_lesiones.models.tipo_lesion_model import TipoLesion
import uuid

def create_tipo_lesion(db: Session, data: dict):
    existente = db.query(TipoLesion).filter(
        (TipoLesion.nombre.ilike(data["nombre"])) |
        (TipoLesion.abreviatura_lesion.ilike(data["abreviatura_lesion"]))
    ).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El tipo de lesión ya existe")

    nuevo = TipoLesion(**data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_tipos_lesion(db: Session):
    return db.query(TipoLesion).all()

def get_tipo_lesion_by_id(db: Session, tipo_lesion_id: uuid.UUID):
    return db.query(TipoLesion).filter(TipoLesion.id == tipo_lesion_id).first()

def update_tipo_lesion(db: Session, tipo_lesion_id: uuid.UUID, data: dict):
    lesion = db.query(TipoLesion).filter(TipoLesion.id == tipo_lesion_id).first()
    if not lesion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de lesión no encontrado")

    for key, value in data.items():
        setattr(lesion, key, value)

    db.commit()
    db.refresh(lesion)
    return lesion

def delete_tipo_lesion(db: Session, tipo_lesion_id: uuid.UUID):
    lesion = db.query(TipoLesion).filter(TipoLesion.id == tipo_lesion_id).first()
    if not lesion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de lesión no encontrado")

    db.delete(lesion)
    db.commit()
    return lesion
