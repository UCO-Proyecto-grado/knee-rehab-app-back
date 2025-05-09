from sqlalchemy.orm import Session
from uuid import UUID
from lambda_terapias.models.estado_plan_rehabilitacion_ejercicio_model import EstadoPlanRehabilitacionEjercicio
from lambda_terapias.schemas.estado_plan_rehabilitacion_ejercicio_schema import EstadoPRECreate, EstadoPREUpdate


def create_estado(db: Session, data: EstadoPRECreate):
    nuevo_estado = EstadoPlanRehabilitacionEjercicio(**data.model_dump())
    db.add(nuevo_estado)
    db.commit()
    db.refresh(nuevo_estado)
    return nuevo_estado


def get_all_estados(db: Session):
    return db.query(EstadoPlanRehabilitacionEjercicio).all()


def get_estado_by_id(db: Session, id: UUID):
    return db.query(EstadoPlanRehabilitacionEjercicio).filter_by(id=id).first()


def update_estado(db: Session, id: UUID, data: EstadoPREUpdate):
    estado = get_estado_by_id(db, id)
    if not estado:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(estado, key, value)
    db.commit()
    db.refresh(estado)
    return estado


def delete_estado(db: Session, id: UUID):
    estado = get_estado_by_id(db, id)
    if estado:
        db.delete(estado)
        db.commit()
    return estado
