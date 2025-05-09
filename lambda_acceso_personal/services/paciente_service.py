from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_acceso_personal.models.paciente_model import Paciente
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)

def create_paciente(db: Session, data: dict):
    logger.info(f"{LogMessages.Paciente.CREATE_ATTEMPT} - Identificación: {data.get('identificacion')}")
    try:
        existente = db.query(Paciente).filter(Paciente.identificacion == data["identificacion"]).first()
        if existente:
            logger.warning(f"{LogMessages.Paciente.DUPLICATE} - Identificación: {data['identificacion']}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Paciente ya registrado")

        paciente = Paciente(**data)
        db.add(paciente)
        db.commit()
        db.refresh(paciente)

        logger.info(f"{LogMessages.Paciente.CREATE_SUCCESS} - ID: {paciente.id}")
        return paciente

    except Exception as e:
        logger.error(f"{LogMessages.Paciente.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear paciente")


def get_pacientes(db: Session):
    logger.info(LogMessages.Paciente.FETCH_ALL)
    try:
        return db.query(Paciente).all()
    except Exception as e:
        logger.error(f"{LogMessages.Paciente.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar pacientes")


def get_paciente_by_id(db: Session, paciente_id: uuid.UUID):
    logger.info(f"{LogMessages.Paciente.FETCH_BY_ID} - ID: {paciente_id}")
    try:
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            logger.warning(f"{LogMessages.Paciente.NOT_FOUND} - ID: {paciente_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")
        return paciente
    except Exception as e:
        logger.error(f"{LogMessages.Paciente.FETCH_BY_ID_FAIL} - ID: {paciente_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar paciente")


def update_paciente(db: Session, paciente_id: uuid.UUID, data: dict):
    logger.info(f"{LogMessages.Paciente.UPDATE_ATTEMPT} - ID: {paciente_id}")
    try:
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            logger.warning(f"{LogMessages.Paciente.NOT_FOUND} - ID: {paciente_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")

        for key, value in data.items():
            setattr(paciente, key, value)

        db.commit()
        db.refresh(paciente)

        logger.info(f"{LogMessages.Paciente.UPDATE_SUCCESS} - ID: {paciente_id}")
        return paciente
    except Exception as e:
        logger.error(f"{LogMessages.Paciente.UPDATE_FAIL} - ID: {paciente_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar paciente")


def delete_paciente(db: Session, paciente_id: uuid.UUID):
    logger.info(f"{LogMessages.Paciente.DELETE_ATTEMPT} - ID: {paciente_id}")
    try:
        paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
        if not paciente:
            logger.warning(f"{LogMessages.Paciente.NOT_FOUND} - ID: {paciente_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")

        db.delete(paciente)
        db.commit()

        logger.info(f"{LogMessages.Paciente.DELETE_SUCCESS} - ID: {paciente_id}")
        return paciente
    except Exception as e:
        logger.error(f"{LogMessages.Paciente.DELETE_FAIL} - ID: {paciente_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar paciente")
