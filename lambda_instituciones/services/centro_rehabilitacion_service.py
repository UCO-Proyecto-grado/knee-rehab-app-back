from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from lambda_instituciones.models.centro_rehabilitacion_model import CentroRehabilitacion
from lambda_instituciones.schemas.centro_rehabilitacion_schema import CentroRehabilitacionUpdate

from uuid import UUID

def _check_centro_constraints(db: Session, identificacion: str, nombre: str, current_id: UUID | None = None):
    query = db.query(CentroRehabilitacion).filter(
        or_(
            func.lower(CentroRehabilitacion.identificacion) == identificacion.lower(),
            func.lower(CentroRehabilitacion.nombre) == nombre.lower()
        )
    )
    if current_id:
        query = query.filter(CentroRehabilitacion.id != current_id)
    
    centro_existente = query.first()
    
    if centro_existente:
        if centro_existente.identificacion.lower() == identificacion.lower():
            raise ValueError("Un centro con esta identificación ya existe")
        elif centro_existente.nombre.lower() == nombre.lower():
            raise ValueError("Un centro con este nombre ya existe")


def create_centro(db: Session, centro: CentroRehabilitacion):
    _check_centro_constraints(db, centro.identificacion, centro.nombre)
    nuevo_centro = CentroRehabilitacion(
        id_tipo_identificacion=centro.id_tipo_identificacion,
        identificacion=centro.identificacion,
        nombre=centro.nombre,
        correo=centro.correo
    )
    db.add(nuevo_centro)
    db.commit()
    db.refresh(nuevo_centro)
    return nuevo_centro

def get_centros(db: Session):
    return db.query(CentroRehabilitacion).all()

def get_centro_by_id(db: Session, centro_id: UUID):
    return db.query(CentroRehabilitacion).filter(CentroRehabilitacion.id == centro_id).first()

def update_centro(db: Session, centro_id: UUID, centro_data: CentroRehabilitacionUpdate):
    if centro_data.identificacion is not None and centro_data.nombre is not None:
        _check_centro_constraints(db, centro_data.identificacion, centro_data.nombre, centro_id)
    elif centro_data.identificacion is not None:
        _check_centro_constraints(db, centro_data.identificacion, "", centro_id)
    elif centro_data.nombre is not None:
        _check_centro_constraints(db, "", centro_data.nombre, centro_id)
    centro = db.query(CentroRehabilitacion).filter(CentroRehabilitacion.id == centro_id).first()
    if not centro:
        return None
    centro_data_dict = centro_data.dict(exclude_unset=True)
    for key, value in centro_data_dict.items():
        setattr(centro, key, value)
    db.commit()
    db.refresh(centro)
    return centro

def delete_centro(db: Session, centro_id: UUID):
    centro = get_centro_by_id(db, centro_id)
    if centro:
        db.delete(centro)
        db.commit()
    return centro
