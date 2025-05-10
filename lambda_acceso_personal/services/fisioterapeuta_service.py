from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_acceso_personal.models.fisioterapeuta_model import Fisioterapeuta
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid
from lambda_instituciones.services.fisioterapeuta_sede_service import create_fisioterapeuta_sede, get_fisioterapeuta_sede_by_sede_id
from lambda_instituciones.schemas.fisioterapeuta_sede_schema import FisioterapeutaSedeCreate
from lambda_instituciones.services import sede_service as instituciones_sede_service

logger = get_logger(__name__)


def create_fisioterapeuta(db: Session, data: dict):
    logger.info(f"{LogMessages.Fisioterapeuta.CREATE_ATTEMPT} - Identificación: {data.get('identificacion')}")
    try:
        existente = db.query(Fisioterapeuta).filter(Fisioterapeuta.identificacion == data["identificacion"]).first()
        if existente:
            logger.warning(f"{LogMessages.Fisioterapeuta.DUPLICATE} - Identificación: {data['identificacion']}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fisioterapeuta ya registrado")

        nuevo = Fisioterapeuta(**data)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.Fisioterapeuta.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo

    except Exception as e:
        logger.error(f"{LogMessages.Fisioterapeuta.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear fisioterapeuta")


def get_fisioterapeutas(db: Session):
    logger.info(LogMessages.Fisioterapeuta.FETCH_ALL)
    try:
        fisioterapeutas = db.query(Fisioterapeuta).all()
        return fisioterapeutas
    except Exception as e:
        logger.error(f"{LogMessages.Fisioterapeuta.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar fisioterapeutas")


def get_fisioterapeutas_filtrados(db: Session, id_sede: uuid.UUID | None = None, id_organizacion: uuid.UUID | None = None):
    fisioterapeuta_ids = set()

    if id_sede:
        fisioterapeuta_sede_relations = get_fisioterapeuta_sede_by_sede_id(db, id_sede)
        for rel in fisioterapeuta_sede_relations:
            fisioterapeuta_ids.add(rel.id_fisioterapeuta)
    elif id_organizacion:
        sedes_en_organizacion = instituciones_sede_service.get_sedes_by_organizacion_id(db, id_organizacion)
        for sede in sedes_en_organizacion:
            fisioterapeuta_sede_relations = get_fisioterapeuta_sede_by_sede_id(db, sede.id)
            for rel in fisioterapeuta_sede_relations:
                fisioterapeuta_ids.add(rel.id_fisioterapeuta)
    else:
        # If no specific filter, return all (or handle as per specific requirements, e.g., empty list)
        return db.query(Fisioterapeuta).all()

    if not fisioterapeuta_ids:
        return []
    
    return db.query(Fisioterapeuta).filter(Fisioterapeuta.id.in_(list(fisioterapeuta_ids))).all()

def get_fisioterapeuta_by_id(db: Session, fisioterapeuta_id: uuid.UUID):
    logger.info(f"{LogMessages.Fisioterapeuta.FETCH_BY_ID} - ID: {fisioterapeuta_id}")
    try:
        fisioterapeuta = db.query(Fisioterapeuta).filter(Fisioterapeuta.id == fisioterapeuta_id).first()
        if not fisioterapeuta:
            logger.warning(f"{LogMessages.Fisioterapeuta.NOT_FOUND} - ID: {fisioterapeuta_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fisioterapeuta no encontrado")
        return fisioterapeuta
    except Exception as e:
        logger.error(f"{LogMessages.Fisioterapeuta.FETCH_BY_ID_FAIL} - ID: {fisioterapeuta_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar fisioterapeuta")


def update_fisioterapeuta(db: Session, fisioterapeuta_id: uuid.UUID, data: dict):
    logger.info(f"{LogMessages.Fisioterapeuta.UPDATE_ATTEMPT} - ID: {fisioterapeuta_id}")
    try:
        f = db.query(Fisioterapeuta).filter(Fisioterapeuta.id == fisioterapeuta_id).first()
        if not f:
            logger.warning(f"{LogMessages.Fisioterapeuta.NOT_FOUND} - ID: {fisioterapeuta_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fisioterapeuta no encontrado")

        for key, value in data.items():
            setattr(f, key, value)

        db.commit()
        db.refresh(f)

        logger.info(f"{LogMessages.Fisioterapeuta.UPDATE_SUCCESS} - ID: {fisioterapeuta_id}")
        return f

    except Exception as e:
        logger.error(f"{LogMessages.Fisioterapeuta.UPDATE_FAIL} - ID: {fisioterapeuta_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar fisioterapeuta")


def delete_fisioterapeuta(db: Session, fisioterapeuta_id: uuid.UUID):
    logger.info(f"{LogMessages.Fisioterapeuta.DELETE_ATTEMPT} - ID: {fisioterapeuta_id}")
    try:
        f = db.query(Fisioterapeuta).filter(Fisioterapeuta.id == fisioterapeuta_id).first()
        if not f:
            logger.warning(f"{LogMessages.Fisioterapeuta.NOT_FOUND} - ID: {fisioterapeuta_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fisioterapeuta no encontrado")

        db.delete(f)
        db.commit()

        logger.info(f"{LogMessages.Fisioterapeuta.DELETE_SUCCESS} - ID: {fisioterapeuta_id}")
        return f

    except Exception as e:
        logger.error(f"{LogMessages.Fisioterapeuta.DELETE_FAIL} - ID: {fisioterapeuta_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar fisioterapeuta")
