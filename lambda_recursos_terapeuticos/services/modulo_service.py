from sqlalchemy.orm import Session
from lambda_recursos_terapeuticos.models.modulo_model import Modulo
from lambda_recursos_terapeuticos.schemas.modulo_schema import ModuloCreate, ModuloUpdate, ModuloOut
from uuid import UUID
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def get_modulos(db: Session, id_centro_rehabilitacion: UUID) -> list[ModuloOut]:
    logger.info(f"{LogMessages.Modulo.FETCH_ALL} - Centro ID: {id_centro_rehabilitacion}")
    try:
        modulos = db.query(Modulo).filter(Modulo.id_centro_rehabilitacion == id_centro_rehabilitacion).all()
        return [ModuloOut.model_validate(m) for m in modulos]
    except Exception as e:
        logger.error(f"{LogMessages.Modulo.FETCH_ALL_FAIL} - Centro ID: {id_centro_rehabilitacion} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar módulos")


def get_modulo_by_id(db: Session, id_modulo: UUID) -> ModuloOut:
    logger.info(f"{LogMessages.Modulo.FETCH_BY_ID} - ID: {id_modulo}")
    try:
        modulo = db.query(Modulo).filter(Modulo.id == id_modulo).first()
        if not modulo:
            logger.warning(f"{LogMessages.Modulo.NOT_FOUND} - ID: {id_modulo}")
            raise HTTPException(status_code=404, detail="Modulo no encontrado")
        return ModuloOut.model_validate(modulo)
    except Exception as e:
        logger.error(f"{LogMessages.Modulo.FETCH_BY_ID_FAIL} - ID: {id_modulo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al buscar módulo")


def create_modulo(db: Session, modulo: ModuloCreate) -> ModuloOut:
    logger.info(f"{LogMessages.Modulo.CREATE_ATTEMPT} - Nombre: {modulo.nombre}")
    try:
        db_modulo = Modulo(**modulo.model_dump(mode="json"))
        db.add(db_modulo)
        db.commit()
        db.refresh(db_modulo)
        logger.info(f"{LogMessages.Modulo.CREATE_SUCCESS} - ID: {db_modulo.id}")
        return ModuloOut.model_validate(db_modulo)
    except Exception as e:
        logger.error(f"{LogMessages.Modulo.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al crear módulo")


def update_modulo(db: Session, id_modulo: UUID, modulo: ModuloUpdate) -> ModuloOut:
    logger.info(f"{LogMessages.Modulo.UPDATE_ATTEMPT} - ID: {id_modulo}")
    try:
        db_modulo = db.query(Modulo).filter(Modulo.id == id_modulo).first()
        if not db_modulo:
            logger.warning(f"{LogMessages.Modulo.NOT_FOUND} - ID: {id_modulo}")
            raise HTTPException(status_code=404, detail="Modulo no encontrado")

        for key, value in modulo.model_dump(exclude_unset=True).items():
            setattr(db_modulo, key, value)

        db.commit()
        db.refresh(db_modulo)
        logger.info(f"{LogMessages.Modulo.UPDATE_SUCCESS} - ID: {id_modulo}")
        return ModuloOut.model_validate(db_modulo)
    except Exception as e:
        logger.error(f"{LogMessages.Modulo.UPDATE_FAIL} - ID: {id_modulo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al actualizar módulo")


def delete_modulo(db: Session, id_modulo: UUID):
    logger.info(f"{LogMessages.Modulo.DELETE_ATTEMPT} - ID: {id_modulo}")
    try:
        db_modulo = db.query(Modulo).filter(Modulo.id == id_modulo).first()
        if not db_modulo:
            logger.warning(f"{LogMessages.Modulo.NOT_FOUND} - ID: {id_modulo}")
            raise HTTPException(status_code=404, detail="Modulo no encontrado")

        db.delete(db_modulo)
        db.commit()
        logger.info(f"{LogMessages.Modulo.DELETE_SUCCESS} - ID: {id_modulo}")
        return {"message": "Modulo eliminado correctamente"}
    except Exception as e:
        logger.error(f"{LogMessages.Modulo.DELETE_FAIL} - ID: {id_modulo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al eliminar módulo")
