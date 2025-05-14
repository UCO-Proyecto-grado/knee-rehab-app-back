from sqlalchemy.orm import Session
from recursos_terapeuticos.app.shared.db.base import MaterialApoyo
from recursos_terapeuticos.app.schemas.recursos_terapeuticos.material_apoyo_schema import MaterialApoyoCreate, MaterialApoyoUpdate, MaterialApoyoOut
from uuid import UUID
from fastapi import HTTPException, status
from recursos_terapeuticos.app.shared.utils.logging_config import get_logger
from recursos_terapeuticos.app.shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def get_material_apoyo(db: Session, id_centro_rehabilitacion: UUID):
    logger.info(f"{LogMessages.MaterialApoyo.FETCH_ALL} - Centro ID: {id_centro_rehabilitacion}")
    try:
        materiales_apoyo = db.query(MaterialApoyo).filter(MaterialApoyo.id_centro_rehabilitacion == id_centro_rehabilitacion).all()
        return [MaterialApoyoOut.model_validate(m) for m in materiales_apoyo]
    except Exception as e:
        logger.error(f"{LogMessages.MaterialApoyo.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar materiales de apoyo")


def get_material_apoyo_by_id(db: Session, id_material_apoyo: UUID) -> MaterialApoyoOut:
    logger.info(f"{LogMessages.MaterialApoyo.FETCH_BY_ID} - ID: {id_material_apoyo}")
    try:
        material_apoyo = db.query(MaterialApoyo).filter(MaterialApoyo.id == id_material_apoyo).first()
        if not material_apoyo:
            logger.warning(f"{LogMessages.MaterialApoyo.NOT_FOUND} - ID: {id_material_apoyo}")
            raise HTTPException(status_code=404, detail="Material de apoyo no encontrado")
        return MaterialApoyoOut.model_validate(material_apoyo)
    except Exception as e:
        logger.error(f"{LogMessages.MaterialApoyo.FETCH_BY_ID_FAIL} - ID: {id_material_apoyo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al buscar material de apoyo")


def create_material_apoyo(db: Session, material_apoyo: MaterialApoyoCreate) -> MaterialApoyoOut:
    logger.info(f"{LogMessages.MaterialApoyo.CREATE_ATTEMPT} - Datos: {material_apoyo}")
    try:
        db_material_apoyo = MaterialApoyo(**material_apoyo.model_dump())
        db.add(db_material_apoyo)
        db.commit()
        db.refresh(db_material_apoyo)
        logger.info(f"{LogMessages.MaterialApoyo.CREATE_SUCCESS} - ID: {db_material_apoyo.id}")
        return MaterialApoyoOut.model_validate(db_material_apoyo)
    except Exception as e:
        logger.error(f"{LogMessages.MaterialApoyo.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al crear material de apoyo")


def update_material_apoyo(db: Session, id_material_apoyo: UUID, material_apoyo: MaterialApoyoUpdate) -> MaterialApoyoOut:
    logger.info(f"{LogMessages.MaterialApoyo.UPDATE_ATTEMPT} - ID: {id_material_apoyo}")
    try:
        material = db.query(MaterialApoyo).filter(MaterialApoyo.id == id_material_apoyo).first()
        if not material:
            logger.warning(f"{LogMessages.MaterialApoyo.NOT_FOUND} - ID: {id_material_apoyo}")
            raise HTTPException(status_code=404, detail="Material de apoyo no encontrado")

        for key, value in material_apoyo.model_dump(exclude_unset=True).items():
            setattr(material, key, value)

        db.commit()
        db.refresh(material)
        logger.info(f"{LogMessages.MaterialApoyo.UPDATE_SUCCESS} - ID: {id_material_apoyo}")
        return MaterialApoyoOut.model_validate(material)
    except Exception as e:
        logger.error(f"{LogMessages.MaterialApoyo.UPDATE_FAIL} - ID: {id_material_apoyo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al actualizar material de apoyo")


def delete_material_apoyo(db: Session, id_material_apoyo: UUID):
    logger.info(f"{LogMessages.MaterialApoyo.DELETE_ATTEMPT} - ID: {id_material_apoyo}")
    try:
        material = db.query(MaterialApoyo).filter(MaterialApoyo.id == id_material_apoyo).first()
        if not material:
            logger.warning(f"{LogMessages.MaterialApoyo.NOT_FOUND} - ID: {id_material_apoyo}")
            raise HTTPException(status_code=404, detail="Material de apoyo no encontrado")

        db.delete(material)
        db.commit()
        logger.info(f"{LogMessages.MaterialApoyo.DELETE_SUCCESS} - ID: {id_material_apoyo}")
        return {"message": "Material de apoyo eliminado correctamente"}
    except Exception as e:
        logger.error(f"{LogMessages.MaterialApoyo.DELETE_FAIL} - ID: {id_material_apoyo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al eliminar material de apoyo")
