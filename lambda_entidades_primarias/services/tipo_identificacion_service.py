from sqlalchemy.orm import Session
from lambda_entidades_primarias.models.tipo_identificacion_model import TipoIdentificacion
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_tipo_identificacion(db: Session, nombre: str, codigo: str):
    logger.info(f"{LogMessages.TipoIdentificacion.CREATE_ATTEMPT} - Nombre: {nombre}, Código: {codigo}")
    try:
        existente = db.query(TipoIdentificacion).filter(
            TipoIdentificacion.nombre.ilike(nombre)
        ).first()
        if existente:
            logger.warning(f"{LogMessages.TipoIdentificacion.DUPLICATE} - Nombre: {nombre}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tipo de identificación ya existe")

        nuevo = TipoIdentificacion(nombre=nombre, codigo=codigo)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.TipoIdentificacion.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except Exception as e:
        logger.error(f"{LogMessages.TipoIdentificacion.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear tipo de identificación")


def get_tipos_identificacion(db: Session):
    logger.info(LogMessages.TipoIdentificacion.FETCH_ALL)
    try:
        return db.query(TipoIdentificacion).all()
    except Exception as e:
        logger.error(f"{LogMessages.TipoIdentificacion.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar tipos de identificación")


def get_tipo_identificacion_by_id(db: Session, tipo_id: uuid.UUID):
    logger.info(f"{LogMessages.TipoIdentificacion.FETCH_BY_ID} - ID: {tipo_id}")
    try:
        tipo = db.query(TipoIdentificacion).filter(TipoIdentificacion.id == tipo_id).first()
        if not tipo:
            logger.warning(f"{LogMessages.TipoIdentificacion.NOT_FOUND} - ID: {tipo_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de identificación no encontrado")
        return tipo
    except Exception as e:
        logger.error(f"{LogMessages.TipoIdentificacion.FETCH_BY_ID_FAIL} - ID: {tipo_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar tipo de identificación")


def update_tipo_identificacion(db: Session, tipo_id: uuid.UUID, nombre: str, codigo: str):
    logger.info(f"{LogMessages.TipoIdentificacion.UPDATE_ATTEMPT} - ID: {tipo_id}")
    try:
        tipo = db.query(TipoIdentificacion).filter(TipoIdentificacion.id == tipo_id).first()
        if not tipo:
            logger.warning(f"{LogMessages.TipoIdentificacion.NOT_FOUND} - ID: {tipo_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de identificación no encontrado")

        tipo.nombre = nombre
        tipo.codigo = codigo
        db.commit()
        db.refresh(tipo)

        logger.info(f"{LogMessages.TipoIdentificacion.UPDATE_SUCCESS} - ID: {tipo_id}")
        return tipo
    except Exception as e:
        logger.error(f"{LogMessages.TipoIdentificacion.UPDATE_FAIL} - ID: {tipo_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar tipo de identificación")


def delete_tipo_identificacion(db: Session, tipo_id: uuid.UUID):
    logger.info(f"{LogMessages.TipoIdentificacion.DELETE_ATTEMPT} - ID: {tipo_id}")
    try:
        tipo = db.query(TipoIdentificacion).filter(TipoIdentificacion.id == tipo_id).first()
        if not tipo:
            logger.warning(f"{LogMessages.TipoIdentificacion.NOT_FOUND} - ID: {tipo_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tipo de identificación no encontrado")

        db.delete(tipo)
        db.commit()

        logger.info(f"{LogMessages.TipoIdentificacion.DELETE_SUCCESS} - ID: {tipo_id}")
        return tipo
    except Exception as e:
        logger.error(f"{LogMessages.TipoIdentificacion.DELETE_FAIL} - ID: {tipo_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar tipo de identificación")
