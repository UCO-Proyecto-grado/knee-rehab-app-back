from sqlalchemy.orm import Session
from lambda_instituciones.models.tipo_sede_model import TipoSede
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_tipo_sede(db: Session, nombre: str):
    logger.info(f"{LogMessages.TipoSede.CREATE_ATTEMPT} - Nombre: {nombre}")
    try:
        tipo_sede_existente = db.query(TipoSede).filter(TipoSede.nombre.ilike(nombre)).first()
        if tipo_sede_existente:
            logger.warning(f"{LogMessages.TipoSede.DUPLICATE} - Nombre: {nombre}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El tipo de sede ya está registrado")

        nuevo = TipoSede(nombre=nombre)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.TipoSede.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except Exception as e:
        logger.error(f"{LogMessages.TipoSede.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear tipo de sede")


def get_tipo_sedes(db: Session):
    logger.info(LogMessages.TipoSede.FETCH_ALL)
    try:
        return db.query(TipoSede).all()
    except Exception as e:
        logger.error(f"{LogMessages.TipoSede.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al listar tipos de sede")


def get_tipo_sede_by_id(db: Session, tipo_sede_id: uuid.UUID):
    logger.info(f"{LogMessages.TipoSede.FETCH_BY_ID} - ID: {tipo_sede_id}")
    try:
        tipo_sede = db.query(TipoSede).filter(TipoSede.id == tipo_sede_id).first()
        if not tipo_sede:
            logger.warning(f"{LogMessages.TipoSede.NOT_FOUND} - ID: {tipo_sede_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de sede no encontrado")
        return tipo_sede
    except Exception as e:
        logger.error(f"{LogMessages.TipoSede.FETCH_BY_ID_FAIL} - ID: {tipo_sede_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar tipo de sede")


def update_tipo_sede(db: Session, tipo_sede_id: uuid.UUID, nombre: str):
    logger.info(f"{LogMessages.TipoSede.UPDATE_ATTEMPT} - ID: {tipo_sede_id}")
    try:
        tipo_sede = db.query(TipoSede).filter(TipoSede.id == tipo_sede_id).first()
        if not tipo_sede:
            logger.warning(f"{LogMessages.TipoSede.NOT_FOUND} - ID: {tipo_sede_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de sede no encontrado")

        tipo_sede.nombre = nombre
        db.commit()
        db.refresh(tipo_sede)

        logger.info(f"{LogMessages.TipoSede.UPDATE_SUCCESS} - ID: {tipo_sede_id}")
        return tipo_sede
    except Exception as e:
        logger.error(f"{LogMessages.TipoSede.UPDATE_FAIL} - ID: {tipo_sede_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar tipo de sede")


def delete_tipo_sede(db: Session, tipo_sede_id: uuid.UUID):
    logger.info(f"{LogMessages.TipoSede.DELETE_ATTEMPT} - ID: {tipo_sede_id}")
    try:
        tipo_sede = db.query(TipoSede).filter(TipoSede.id == tipo_sede_id).first()
        if not tipo_sede:
            logger.warning(f"{LogMessages.TipoSede.NOT_FOUND} - ID: {tipo_sede_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de sede no encontrado")

        db.delete(tipo_sede)
        db.commit()

        logger.info(f"{LogMessages.TipoSede.DELETE_SUCCESS} - ID: {tipo_sede_id}")
        return tipo_sede
    except Exception as e:
        logger.error(f"{LogMessages.TipoSede.DELETE_FAIL} - ID: {tipo_sede_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar tipo de sede")
