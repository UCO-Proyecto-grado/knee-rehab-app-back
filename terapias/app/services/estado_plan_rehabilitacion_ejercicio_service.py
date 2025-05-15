from sqlalchemy.orm import Session
from uuid import UUID
from terapias.app.shared.db.base import EstadoPlanRehabilitacionEjercicio
from terapias.app.schemas.terapias.estado_plan_rehabilitacion_ejercicio_schema import EstadoPRECreate, EstadoPREUpdate
from fastapi import HTTPException, status
from terapias.app.shared.utils.logging_config import get_logger
from terapias.app.shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def create_estado(db: Session, data: EstadoPRECreate):
    logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.CREATE_ATTEMPT}")
    try:
        nuevo = EstadoPlanRehabilitacionEjercicio(**data.model_dump())
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except Exception as e:
        logger.error(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al crear estado")


def get_all_estados(db: Session):
    logger.info(LogMessages.EstadoPlanRehabilitacionEjercicio.FETCH_ALL)
    try:
        return db.query(EstadoPlanRehabilitacionEjercicio).all()
    except Exception as e:
        logger.error(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar estados")


def get_estado_by_id(db: Session, id: UUID):
    logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.FETCH_BY_ID} - ID: {id}")
    try:
        estado = db.query(EstadoPlanRehabilitacionEjercicio).filter_by(id=id).first()
        if not estado:
            logger.warning(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.NOT_FOUND} - ID: {id}")
            raise HTTPException(status_code=404, detail="Estado no encontrado")
        return estado
    except Exception as e:
        logger.error(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.FETCH_BY_ID_FAIL} - ID: {id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al buscar estado")


def update_estado(db: Session, id: UUID, data: EstadoPREUpdate):
    logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.UPDATE_ATTEMPT} - ID: {id}")
    try:
        estado = db.query(EstadoPlanRehabilitacionEjercicio).filter_by(id=id).first()
        if not estado:
            logger.warning(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.NOT_FOUND} - ID: {id}")
            raise HTTPException(status_code=404, detail="Estado no encontrado")

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(estado, key, value)

        db.commit()
        db.refresh(estado)
        logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.UPDATE_SUCCESS} - ID: {id}")
        return estado
    except Exception as e:
        logger.error(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.UPDATE_FAIL} - ID: {id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al actualizar estado")


def delete_estado(db: Session, id: UUID):
    logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.DELETE_ATTEMPT} - ID: {id}")
    try:
        estado = db.query(EstadoPlanRehabilitacionEjercicio).filter_by(id=id).first()
        if not estado:
            logger.warning(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.NOT_FOUND} - ID: {id}")
            raise HTTPException(status_code=404, detail="Estado no encontrado")

        db.delete(estado)
        db.commit()
        logger.info(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.DELETE_SUCCESS} - ID: {id}")
        return estado
    except Exception as e:
        logger.error(f"{LogMessages.EstadoPlanRehabilitacionEjercicio.DELETE_FAIL} - ID: {id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al eliminar estado")
