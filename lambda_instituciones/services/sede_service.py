from sqlalchemy.orm import Session
from uuid import UUID
from lambda_instituciones.models.sede_model import Sede
from lambda_instituciones.schemas.sede_schema import SedeCreate, SedeUpdate
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def create_sede(db: Session, sede_data: SedeCreate):
    logger.info(f"{LogMessages.Sede.CREATE_ATTEMPT} - Nombre: {sede_data.nombre}")
    try:
        nueva_sede = Sede(**sede_data.model_dump())
        db.add(nueva_sede)
        db.commit()
        db.refresh(nueva_sede)

        logger.info(f"{LogMessages.Sede.CREATE_SUCCESS} - ID: {nueva_sede.id}")
        return nueva_sede
    except Exception as e:
        logger.error(f"{LogMessages.Sede.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear sede")


def get_sedes(db: Session):
    logger.info(LogMessages.Sede.FETCH_ALL)
    try:
        return db.query(Sede).all()
    except Exception as e:
        logger.error(f"{LogMessages.Sede.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar sedes")


def get_sede_by_id(db: Session, sede_id: UUID):
    logger.info(f"{LogMessages.Sede.FETCH_BY_ID} - ID: {sede_id}")
    try:
        sede = db.query(Sede).filter(Sede.id == sede_id).first()
        if not sede:
            logger.warning(f"{LogMessages.Sede.NOT_FOUND} - ID: {sede_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")
        return sede
    except Exception as e:
        logger.error(f"{LogMessages.Sede.FETCH_BY_ID_FAIL} - ID: {sede_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar sede")


def update_sede(db: Session, sede_id: UUID, sede_data: SedeUpdate):
    logger.info(f"{LogMessages.Sede.UPDATE_ATTEMPT} - ID: {sede_id}")
    try:
        sede = get_sede_by_id(db, sede_id)
        if not sede:
            logger.warning(f"{LogMessages.Sede.NOT_FOUND} - ID: {sede_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")

        for key, value in sede_data.model_dump(exclude_unset=True).items():
            setattr(sede, key, value)

        db.commit()
        db.refresh(sede)

        logger.info(f"{LogMessages.Sede.UPDATE_SUCCESS} - ID: {sede_id}")
        return sede
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.Sede.UPDATE_FAIL} - ID: {sede_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar sede")


def delete_sede(db: Session, sede_id: UUID):
    logger.info(f"{LogMessages.Sede.DELETE_ATTEMPT} - ID: {sede_id}")
    try:
        sede = get_sede_by_id(db, sede_id)
        if not sede:
            logger.warning(f"{LogMessages.Sede.NOT_FOUND} - ID: {sede_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sede no encontrada")

        db.delete(sede)
        db.commit()

        logger.info(f"{LogMessages.Sede.DELETE_SUCCESS} - ID: {sede_id}")
        return sede
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.Sede.DELETE_FAIL} - ID: {sede_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar sede")
