from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_acceso_personal.models.fisioterapeuta_model import Fisioterapeuta
import uuid
from lambda_instituciones.services.fisioterapeuta_sede_service import create_fisioterapeuta_sede, get_fisioterapeuta_sede_by_sede_id
from lambda_instituciones.schemas.fisioterapeuta_sede_schema import FisioterapeutaSedeCreate
from lambda_instituciones.services import sede_service as instituciones_sede_service

def create_fisioterapeuta(db: Session, data: dict, id_sede: uuid.UUID | None = None):
    existente = db.query(Fisioterapeuta).filter(Fisioterapeuta.identificacion == data["identificacion"]).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fisioterapeuta ya registrado")

    nuevo_fisioterapeuta_data = data.copy() # Create a copy to avoid modifying the original dict
    nuevo = Fisioterapeuta(**nuevo_fisioterapeuta_data)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    if id_sede:
        fisioterapeuta_sede_data = FisioterapeutaSedeCreate(
            id_fisioterapeuta=nuevo.id,
            id_sede=id_sede
        )
        create_fisioterapeuta_sede(db=db, data=fisioterapeuta_sede_data)

    return nuevo

def get_fisioterapeutas(db: Session):
    return db.query(Fisioterapeuta).all()

def get_fisioterapeutas_filtrados(db: Session, id_sede: uuid.UUID | None = None, id_organizacion: uuid.UUID | None = None):
    fisioterapeuta_ids = set()

    if id_sede:
        fisioterapeuta_sede_relations = get_fisioterapeuta_sede_by_sede_id(db, id_sede)
        for rel in fisioterapeuta_sede_relations:
            fisioterapeuta_ids.add(rel.id_fisioterapeuta)
    elif id_organizacion:
        sedes_en_organizacion = instituciones_sede_service.get_sedes_by_organizacion_id(db, id_organizacion)
        for sede in sedes_en_organizacion:
            fisioterapeuta_sede_relations = get_fisioterapeuta_sede_by_sede_id(db, sede.id)
            for rel in fisioterapeuta_sede_relations:
                fisioterapeuta_ids.add(rel.id_fisioterapeuta)
    else:
        # If no specific filter, return all (or handle as per specific requirements, e.g., empty list)
        return db.query(Fisioterapeuta).all()

    if not fisioterapeuta_ids:
        return []
    
    return db.query(Fisioterapeuta).filter(Fisioterapeuta.id.in_(list(fisioterapeuta_ids))).all()

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
