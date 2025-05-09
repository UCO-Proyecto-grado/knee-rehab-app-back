from sqlalchemy.orm import Session
from lambda_recursos_terapeuticos.models.material_apoyo_model import MaterialApoyo
from lambda_recursos_terapeuticos.schemas.material_apoyo_schema import MaterialApoyoCreate, MaterialApoyoUpdate, MaterialApoyoOut
from uuid import UUID
from fastapi import HTTPException

def get_material_apoyo(db: Session, id_centro_rehabilitacion: UUID):
    materiales_apoyo = db.query(MaterialApoyo).filter(MaterialApoyo.id_centro_rehabilitacion == id_centro_rehabilitacion).all()
    return [MaterialApoyoOut.model_validate(m) for m in materiales_apoyo]

def get_material_apoyo_by_id(db: Session, id_material_apoyo: UUID) -> MaterialApoyoOut:
    material_apoyo = db.query(MaterialApoyo).filter(MaterialApoyo.id == id_material_apoyo).first()
    if not material_apoyo:
        raise HTTPException(status_code=404, detail="Material de apoyo no encontrado")
    return MaterialApoyoOut.model_validate(material_apoyo)

def create_material_apoyo(db: Session, material_apoyo: MaterialApoyoCreate) -> MaterialApoyoOut:
    db_material_apoyo = MaterialApoyo(**material_apoyo.model_dump())
    db.add(db_material_apoyo)
    db.commit()
    db.refresh(db_material_apoyo)
    return MaterialApoyoOut.model_validate(db_material_apoyo)

def update_material_apoyo(db: Session, id_material_apoyo: UUID, material_apoyo: MaterialApoyoUpdate) -> MaterialApoyoOut:
    db_material_apoyo = get_material_apoyo_by_id(db, id_material_apoyo)
    if not db_material_apoyo:
        raise HTTPException(status_code=404, detail="Material de apoyo no encontrado")
    db_material_apoyo.update(material_apoyo.model_dump(mode="json"))
    db.commit()
    db.refresh(db_material_apoyo)
    return MaterialApoyoOut.model_validate(db_material_apoyo)

def delete_material_apoyo(db: Session, id_material_apoyo: UUID):
    db_material_apoyo = get_material_apoyo_by_id(db, id_material_apoyo)
    if not db_material_apoyo:
        raise HTTPException(status_code=404, detail="Material de apoyo no encontrado")
    db.delete(db_material_apoyo)
    db.commit()
    return {"message": "Material de apoyo eliminado correctamente"}