from sqlalchemy.orm import Session
from entidades_primarias.app.models.pais_model import Pais
from fastapi import HTTPException, status
from entidades_primarias.app.shared.utils.logging_config import get_logger
from entidades_primarias.app.shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_pais(db: Session, nombre: str):
    logger.info(f"{LogMessages.Pais.CREATE_ATTEMPT} - Nombre: {nombre}")
    try:
        pais_existente = db.query(Pais).filter(Pais.nombre.ilike(nombre)).first()
        if pais_existente:
            logger.warning(f"{LogMessages.Pais.DUPLICATE} - Nombre: {nombre}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El país ya está registrado")

        nuevo_pais = Pais(nombre=nombre)
        db.add(nuevo_pais)
        db.commit()
        db.refresh(nuevo_pais)

        logger.info(f"{LogMessages.Pais.CREATE_SUCCESS} - ID: {nuevo_pais.id}")
        return nuevo_pais
    except Exception as e:
        logger.error(f"{LogMessages.Pais.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear país")


def get_paises(db: Session):
    logger.info(LogMessages.Pais.FETCH_ALL)
    try:
        return db.query(Pais).all()
    except Exception as e:
        logger.error(f"{LogMessages.Pais.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar países")


def get_pais_by_id(db: Session, pais_id: uuid.UUID):
    logger.info(f"{LogMessages.Pais.FETCH_BY_ID} - ID: {pais_id}")
    try:
        pais = db.query(Pais).filter(Pais.id == pais_id).first()
        if not pais:
            logger.warning(f"{LogMessages.Pais.NOT_FOUND} - ID: {pais_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="País no encontrado")
        return pais
    except Exception as e:
        logger.error(f"{LogMessages.Pais.FETCH_BY_ID_FAIL} - ID: {pais_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar país")


def update_pais(db: Session, pais_id: uuid.UUID, nombre: str):
    logger.info(f"{LogMessages.Pais.UPDATE_ATTEMPT} - ID: {pais_id}")
    try:
        pais = db.query(Pais).filter(Pais.id == pais_id).first()
        if not pais:
            logger.warning(f"{LogMessages.Pais.NOT_FOUND} - ID: {pais_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="País no encontrado")

        pais.nombre = nombre
        db.commit()
        db.refresh(pais)

        logger.info(f"{LogMessages.Pais.UPDATE_SUCCESS} - ID: {pais_id}")
        return pais
    except Exception as e:
        logger.error(f"{LogMessages.Pais.UPDATE_FAIL} - ID: {pais_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar país")


def delete_pais(db: Session, pais_id: uuid.UUID):
    logger.info(f"{LogMessages.Pais.DELETE_ATTEMPT} - ID: {pais_id}")
    try:
        pais = db.query(Pais).filter(Pais.id == pais_id).first()
        if not pais:
            logger.warning(f"{LogMessages.Pais.NOT_FOUND} - ID: {pais_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="País no encontrado")

        db.delete(pais)
        db.commit()

        logger.info(f"{LogMessages.Pais.DELETE_SUCCESS} - ID: {pais_id}")
        return pais
    except Exception as e:
        logger.error(f"{LogMessages.Pais.DELETE_FAIL} - ID: {pais_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar país")
