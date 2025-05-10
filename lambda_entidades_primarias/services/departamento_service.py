from sqlalchemy.orm import Session, joinedload
from lambda_entidades_primarias.models.departamento_model import Departamento
from lambda_entidades_primarias.models.pais_model import Pais
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_departamento(db: Session, nombre: str, id_pais: uuid.UUID):
    logger.info(f"{LogMessages.Departamento.CREATE_ATTEMPT} - Nombre: {nombre}, País ID: {id_pais}")
    try:
        pais = db.query(Pais).filter(Pais.id == id_pais).first()
        if not pais:
            logger.warning(f"{LogMessages.Departamento.PAIS_NOT_FOUND} - ID: {id_pais}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="País no encontrado")

        existente = db.query(Departamento).filter(
            Departamento.nombre.ilike(nombre),
            Departamento.id_pais == id_pais
        ).first()
        if existente:
            logger.warning(f"{LogMessages.Departamento.DUPLICATE} - Nombre: {nombre}, País ID: {id_pais}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El departamento ya está registrado para este país")

        nuevo = Departamento(nombre=nombre, id_pais=id_pais)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.Departamento.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except Exception as e:
        logger.error(f"{LogMessages.Departamento.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear departamento")


def get_departamentos(db: Session):
    logger.info(LogMessages.Departamento.FETCH_ALL)
    try:
        return db.query(Departamento).options(joinedload(Departamento.pais)).all()
    except Exception as e:
        logger.error(f"{LogMessages.Departamento.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar departamentos")


def get_departamento_by_id(db: Session, departamento_id: uuid.UUID):
    logger.info(f"{LogMessages.Departamento.FETCH_BY_ID} - ID: {departamento_id}")
    try:
        departamento = db.query(Departamento).options(joinedload(Departamento.pais)).filter(Departamento.id == departamento_id).first()
        if not departamento:
            logger.warning(f"{LogMessages.Departamento.NOT_FOUND} - ID: {departamento_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")
        return departamento
    except Exception as e:
        logger.error(f"{LogMessages.Departamento.FETCH_BY_ID_FAIL} - ID: {departamento_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al consultar departamento")


def update_departamento(db: Session, departamento_id: uuid.UUID, nombre: str, id_pais: uuid.UUID):
    logger.info(f"{LogMessages.Departamento.UPDATE_ATTEMPT} - ID: {departamento_id}")
    try:
        departamento = db.query(Departamento).filter(Departamento.id == departamento_id).first()
        if not departamento:
            logger.warning(f"{LogMessages.Departamento.NOT_FOUND} - ID: {departamento_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")

        departamento.nombre = nombre
        departamento.id_pais = id_pais
        db.commit()
        db.refresh(departamento)

        logger.info(f"{LogMessages.Departamento.UPDATE_SUCCESS} - ID: {departamento_id}")
        return departamento
    except Exception as e:
        logger.error(f"{LogMessages.Departamento.UPDATE_FAIL} - ID: {departamento_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar departamento")


def delete_departamento(db: Session, departamento_id: uuid.UUID):
    logger.info(f"{LogMessages.Departamento.DELETE_ATTEMPT} - ID: {departamento_id}")
    try:
        departamento = db.query(Departamento).filter(Departamento.id == departamento_id).first()
        if not departamento:
            logger.warning(f"{LogMessages.Departamento.NOT_FOUND} - ID: {departamento_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Departamento no encontrado")

        db.delete(departamento)
        db.commit()

        logger.info(f"{LogMessages.Departamento.DELETE_SUCCESS} - ID: {departamento_id}")
        return departamento
    except Exception as e:
        logger.error(f"{LogMessages.Departamento.DELETE_FAIL} - ID: {departamento_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar departamento")
