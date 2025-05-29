from sqlalchemy.orm import Session, joinedload
from entidades_primarias.app.models.ciudad_model import Ciudad
from entidades_primarias.app.models.departamento_model import Departamento
from fastapi import HTTPException, status
from entidades_primarias.app.shared.utils.logging_config import get_logger
from entidades_primarias.app.shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_ciudad(db: Session, nombre: str, id_departamento: uuid.UUID):
    logger.info(f"{LogMessages.Ciudad.CREATE_ATTEMPT} - Nombre: {nombre} - Departamento ID: {id_departamento}")
    try:
        dep = db.query(Departamento).filter(Departamento.id == id_departamento).first()
        if not dep:
            logger.warning(f"{LogMessages.Ciudad.DEPARTAMENTO_NOT_FOUND} - ID: {id_departamento}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")

        existente = db.query(Ciudad).filter(
            Ciudad.nombre.ilike(nombre),
            Ciudad.id_departamento == id_departamento
        ).first()
        if existente:
            logger.warning(f"{LogMessages.Ciudad.DUPLICATE} - Nombre: {nombre} - Departamento ID: {id_departamento}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La ciudad ya existe en ese departamento")

        nueva = Ciudad(nombre=nombre, id_departamento=id_departamento)
        db.add(nueva)
        db.commit()
        db.refresh(nueva)

        logger.info(f"{LogMessages.Ciudad.CREATE_SUCCESS} - ID: {nueva.id}")
        return nueva

    except Exception as e:
        logger.error(f"{LogMessages.Ciudad.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear ciudad")


def get_ciudades(db: Session):
    logger.info(LogMessages.Ciudad.FETCH_ALL)
    try:
        return db.query(Ciudad).options(joinedload(Ciudad.departamento)).all()
    except Exception as e:
        logger.error(f"{LogMessages.Ciudad.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar ciudades")


def get_ciudad_by_id(db: Session, ciudad_id: uuid.UUID):
    logger.info(f"{LogMessages.Ciudad.FETCH_BY_ID} - ID: {ciudad_id}")
    try:
        ciudad = db.query(Ciudad).options(joinedload(Ciudad.departamento)).filter(Ciudad.id == ciudad_id).first()
        if not ciudad:
            logger.warning(f"{LogMessages.Ciudad.NOT_FOUND} - ID: {ciudad_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")
        return ciudad
    except Exception as e:
        logger.error(f"{LogMessages.Ciudad.FETCH_BY_ID_FAIL} - ID: {ciudad_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar ciudad")


def update_ciudad(db: Session, ciudad_id: uuid.UUID, nombre: str, id_departamento: uuid.UUID):
    logger.info(f"{LogMessages.Ciudad.UPDATE_ATTEMPT} - ID: {ciudad_id}")
    try:
        ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
        if not ciudad:
            logger.warning(f"{LogMessages.Ciudad.NOT_FOUND} - ID: {ciudad_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")

        ciudad.nombre = nombre
        ciudad.id_departamento = id_departamento
        db.commit()
        db.refresh(ciudad)

        logger.info(f"{LogMessages.Ciudad.UPDATE_SUCCESS} - ID: {ciudad_id}")
        return ciudad

    except Exception as e:
        logger.error(f"{LogMessages.Ciudad.UPDATE_FAIL} - ID: {ciudad_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar ciudad")


def delete_ciudad(db: Session, ciudad_id: uuid.UUID):
    logger.info(f"{LogMessages.Ciudad.DELETE_ATTEMPT} - ID: {ciudad_id}")
    try:
        ciudad = db.query(Ciudad).filter(Ciudad.id == ciudad_id).first()
        if not ciudad:
            logger.warning(f"{LogMessages.Ciudad.NOT_FOUND} - ID: {ciudad_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ciudad no encontrada")

        db.delete(ciudad)
        db.commit()

        logger.info(f"{LogMessages.Ciudad.DELETE_SUCCESS} - ID: {ciudad_id}")
        return ciudad

    except Exception as e:
        logger.error(f"{LogMessages.Ciudad.DELETE_FAIL} - ID: {ciudad_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar ciudad")
