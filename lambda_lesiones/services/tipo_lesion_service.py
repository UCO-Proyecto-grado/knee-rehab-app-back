from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_lesiones.models.tipo_lesion_model import TipoLesion
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_tipo_lesion(db: Session, data: dict):
    logger.info(f"{LogMessages.TipoLesion.CREATE_ATTEMPT} - Nombre: {data.get('nombre')}")
    try:
        existente = db.query(TipoLesion).filter(
            (TipoLesion.nombre.ilike(data["nombre"])) |
            (TipoLesion.abreviatura_lesion.ilike(data["abreviatura_lesion"]))
        ).first()

        if existente:
            logger.warning(f"{LogMessages.TipoLesion.DUPLICATE} - Nombre o abreviatura duplicada")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El tipo de lesión ya existe")

        nuevo = TipoLesion(**data)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.TipoLesion.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except Exception as e:
        logger.error(f"{LogMessages.TipoLesion.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear tipo de lesión")


def get_tipos_lesion(db: Session):
    logger.info(LogMessages.TipoLesion.FETCH_ALL)
    try:
        return db.query(TipoLesion).all()
    except Exception as e:
        logger.error(f"{LogMessages.TipoLesion.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar tipos de lesión")


def get_tipo_lesion_by_id(db: Session, tipo_lesion_id: uuid.UUID):
    logger.info(f"{LogMessages.TipoLesion.FETCH_BY_ID} - ID: {tipo_lesion_id}")
    try:
        lesion = db.query(TipoLesion).filter(TipoLesion.id == tipo_lesion_id).first()
        if not lesion:
            logger.warning(f"{LogMessages.TipoLesion.NOT_FOUND} - ID: {tipo_lesion_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de lesión no encontrado")
        return lesion
    except Exception as e:
        logger.error(f"{LogMessages.TipoLesion.FETCH_BY_ID_FAIL} - ID: {tipo_lesion_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar tipo de lesión")


def update_tipo_lesion(db: Session, tipo_lesion_id: uuid.UUID, data: dict):
    logger.info(f"{LogMessages.TipoLesion.UPDATE_ATTEMPT} - ID: {tipo_lesion_id}")
    try:
        lesion = db.query(TipoLesion).filter(TipoLesion.id == tipo_lesion_id).first()
        if not lesion:
            logger.warning(f"{LogMessages.TipoLesion.NOT_FOUND} - ID: {tipo_lesion_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de lesión no encontrado")

        for key, value in data.items():
            setattr(lesion, key, value)

        db.commit()
        db.refresh(lesion)

        logger.info(f"{LogMessages.TipoLesion.UPDATE_SUCCESS} - ID: {tipo_lesion_id}")
        return lesion
    except Exception as e:
        logger.error(f"{LogMessages.TipoLesion.UPDATE_FAIL} - ID: {tipo_lesion_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar tipo de lesión")


def delete_tipo_lesion(db: Session, tipo_lesion_id: uuid.UUID):
    logger.info(f"{LogMessages.TipoLesion.DELETE_ATTEMPT} - ID: {tipo_lesion_id}")
    try:
        lesion = db.query(TipoLesion).filter(TipoLesion.id == tipo_lesion_id).first()
        if not lesion:
            logger.warning(f"{LogMessages.TipoLesion.NOT_FOUND} - ID: {tipo_lesion_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de lesión no encontrado")

        db.delete(lesion)
        db.commit()

        logger.info(f"{LogMessages.TipoLesion.DELETE_SUCCESS} - ID: {tipo_lesion_id}")
        return lesion
    except Exception as e:
        logger.error(f"{LogMessages.TipoLesion.DELETE_FAIL} - ID: {tipo_lesion_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar tipo de lesión")
