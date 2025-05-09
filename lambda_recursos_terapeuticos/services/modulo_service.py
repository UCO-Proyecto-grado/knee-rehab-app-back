from sqlalchemy.orm import Session
from lambda_recursos_terapeuticos.models.modulo_model import Modulo
from lambda_recursos_terapeuticos.schemas.modulo_schema import ModuloCreate, ModuloUpdate, ModuloOut
from uuid import UUID
from fastapi import HTTPException

def get_modulos(db: Session, id_centro_rehabilitacion: UUID) -> list[ModuloOut]:
    modulos = db.query(Modulo).filter(Modulo.id_centro_rehabilitacion == id_centro_rehabilitacion).all()
    return [ModuloOut.model_validate(m) for m in modulos]

def get_modulo_by_id(db: Session, id_modulo: UUID) -> ModuloOut:
    modulo = db.query(Modulo).filter(Modulo.id == id_modulo).first()
    if not modulo:
        raise HTTPException(status_code=404, detail="Modulo no encontrado")
    return ModuloOut.model_validate(modulo)

def create_modulo(db: Session, modulo: ModuloCreate) -> ModuloOut:
    db_modulo = Modulo(**modulo.model_dump(mode="json"))
    db.add(db_modulo)
    db.commit()
    db.refresh(db_modulo)
    return ModuloOut.model_validate(db_modulo)


def update_modulo(db: Session, id_modulo: UUID, modulo: ModuloUpdate) -> ModuloOut:
    db_modulo = get_modulo_by_id(db, id_modulo)
    if not db_modulo:
        raise HTTPException(status_code=404, detail="Modulo no encontrado")
    db_modulo.update(modulo.model_dump(mode="json"))
    db.commit()
    db.refresh(db_modulo)
    return ModuloOut.model_validate(db_modulo)

def delete_modulo(db: Session, id_modulo: UUID):
    db_modulo = get_modulo_by_id(db, id_modulo)
    if not db_modulo:
        raise HTTPException(status_code=404, detail="Modulo no encontrado")
    db.delete(db_modulo)
    db.commit()
    return {"message": "Modulo eliminado correctamente"}