from sqlalchemy.orm import Session
from uuid import UUID
from lambda_instituciones.models.sede_model import Sede
from lambda_instituciones.schemas.sede_schema import SedeCreate, SedeUpdate


def create_sede(db: Session, sede_data: SedeCreate):
    nueva_sede = Sede(**sede_data.model_dump())
    db.add(nueva_sede)
    db.commit()
    db.refresh(nueva_sede)
    return nueva_sede


def get_sedes(db: Session):
    return db.query(Sede).all()


def get_sede_by_id(db: Session, sede_id: UUID):
    return db.query(Sede).filter(Sede.id == sede_id).first()


def update_sede(db: Session, sede_id: UUID, sede_data: SedeUpdate):
    sede = get_sede_by_id(db, sede_id)
    if not sede:
        return None
    for key, value in sede_data.model_dump(exclude_unset=True).items():
        setattr(sede, key, value)
    db.commit()
    db.refresh(sede)
    return sede


def delete_sede(db: Session, sede_id: UUID):
    sede = get_sede_by_id(db, sede_id)
    if sede:
        db.delete(sede)
        db.commit()
    return sede
