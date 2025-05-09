from sqlalchemy.orm import Session
from lambda_recursos_terapeuticos.models.ejercicio_model import Ejercicio
from lambda_recursos_terapeuticos.schemas.ejercicio_schema import EjercicioCreate, EjercicioUpdate, EjercicioOut
from uuid import UUID
from sqlalchemy.orm import selectinload
from lambda_recursos_terapeuticos.models.modulo_model import Modulo

from fastapi import HTTPException

def get_ejercicio(db: Session, id_modulo: UUID):    
    ejercicios = db.query(Ejercicio).filter(Ejercicio.id_modulo == id_modulo).all()
    return [EjercicioOut.model_validate(e) for e in ejercicios]

def get_ejercicio_by_id(db: Session, id_ejercicio: UUID) -> EjercicioOut:
    ejercicio = db.query(Ejercicio).filter(Ejercicio.id == id_ejercicio).first()
    if not ejercicio:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
    return EjercicioOut.model_validate(ejercicio)

def create_ejercicio(db: Session, ejercicio: EjercicioCreate) -> EjercicioOut:
    db_ejercicio = Ejercicio(**ejercicio.model_dump())
    db.add(db_ejercicio)
    db.commit()
    db.refresh(db_ejercicio)
    return EjercicioOut.model_validate(db_ejercicio)

def update_ejercicio(db: Session, id_ejercicio: UUID, ejercicio: EjercicioUpdate) -> EjercicioOut:
    db_ejercicio = db.query(Ejercicio).filter(Ejercicio.id == id_ejercicio).first()
    if not db_ejercicio:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado")

    for key, value in ejercicio.model_dump(exclude_unset=True).items():
        setattr(db_ejercicio, key, value)

    db.commit()
    db.refresh(db_ejercicio)
    return EjercicioOut.model_validate(db_ejercicio)

def delete_ejercicio(db: Session, id_ejercicio: UUID):
    db_ejercicio = get_ejercicio_by_id(db, id_ejercicio)
    if not db_ejercicio:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
    db.delete(db_ejercicio)
    db.commit()
    return {"message": "Ejercicio eliminado correctamente"}

def get_ejercicio_por_centro_rehabilitacion(db: Session, id_centro_rehabilitacion: UUID) -> list[EjercicioOut]:
    ejercicios = (
        db.query(Ejercicio)
        .join(Ejercicio.modulo)
        .filter(Modulo.id_centro_rehabilitacion == id_centro_rehabilitacion)
        .options(selectinload(Ejercicio.modulo))
        .all()
    )
    return [EjercicioOut.model_validate(e) for e in ejercicios]

def get_ejercicio_por_centro_rehabilitacion_y_modulo(db: Session, id_centro_rehabilitacion: UUID, id_modulo: UUID) -> list[EjercicioOut]:
    ejercicios = (
        db.query(Ejercicio)
        .join(Ejercicio.modulo)
        .filter(Modulo.id_centro_rehabilitacion == id_centro_rehabilitacion, Ejercicio.id_modulo == id_modulo)
        .options(selectinload(Ejercicio.modulo))
        .all()
    )
    return [EjercicioOut.model_validate(e) for e in ejercicios]