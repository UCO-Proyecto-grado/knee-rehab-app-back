from sqlalchemy.orm import Session
from lambda_entidades_primarias.models.estado_model import Estado
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_estado(db: Session, nombre: str):
    logger.info(f"{LogMessages.Estado.CREATE_ATTEMPT} - Nombre: {nombre}")
    try:
        existente = db.query(Estado).filter(Estado.nombre.ilike(nombre)).first()
        if existente:
            logger.warning(f"{LogMessages.Estado.DUPLICATE} - Nombre: {nombre}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El estado ya existe")

        nuevo = Estado(nombre=nombre)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.Estado.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except Exception as e:
        logger.error(f"{LogMessages.Estado.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear estado")


def get_estados(db: Session):
    logger.info(LogMessages.Estado.FETCH_ALL)
    try:
        return db.query(Estado).all()
    except Exception as e:
        logger.error(f"{LogMessages.Estado.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar estados")


def get_estado_by_id(db: Session, estado_id: uuid.UUID):
    logger.info(f"{LogMessages.Estado.FETCH_BY_ID} - ID: {estado_id}")
    try:
        estado = db.query(Estado).filter(Estado.id == estado_id).first()
        if not estado:
            logger.warning(f"{LogMessages.Estado.NOT_FOUND} - ID: {estado_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")
        return estado
    except Exception as e:
        logger.error(f"{LogMessages.Estado.FETCH_BY_ID_FAIL} - ID: {estado_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar estado")


def update_estado(db: Session, estado_id: uuid.UUID, nombre: str):
    logger.info(f"{LogMessages.Estado.UPDATE_ATTEMPT} - ID: {estado_id}")
    try:
        estado = db.query(Estado).filter(Estado.id == estado_id).first()
        if not estado:
            logger.warning(f"{LogMessages.Estado.NOT_FOUND} - ID: {estado_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")

        estado.nombre = nombre
        db.commit()
        db.refresh(estado)

        logger.info(f"{LogMessages.Estado.UPDATE_SUCCESS} - ID: {estado_id}")
        return estado
    except Exception as e:
        logger.error(f"{LogMessages.Estado.UPDATE_FAIL} - ID: {estado_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar estado")


def delete_estado(db: Session, estado_id: uuid.UUID):
    logger.info(f"{LogMessages.Estado.DELETE_ATTEMPT} - ID: {estado_id}")
    try:
        estado = db.query(Estado).filter(Estado.id == estado_id).first()
        if not estado:
            logger.warning(f"{LogMessages.Estado.NOT_FOUND} - ID: {estado_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estado no encontrado")

        db.delete(estado)
        db.commit()

        logger.info(f"{LogMessages.Estado.DELETE_SUCCESS} - ID: {estado_id}")
        return estado
    except Exception as e:
        logger.error(f"{LogMessages.Estado.DELETE_FAIL} - ID: {estado_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar estado")
