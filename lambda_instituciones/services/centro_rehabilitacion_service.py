from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from lambda_instituciones.models.centro_rehabilitacion_model import CentroRehabilitacion
from lambda_instituciones.schemas.centro_rehabilitacion_schema import CentroRehabilitacionUpdate, CentroRehabilitacionBase as CentroRehabilitacionIn
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages
from uuid import UUID

logger = get_logger(__name__)


def _check_centro_constraints(db: Session, identificacion: str, nombre: str, current_id: UUID | None = None):
    query = db.query(CentroRehabilitacion).filter(
        or_(
            func.lower(CentroRehabilitacion.identificacion) == identificacion.lower(),
            func.lower(CentroRehabilitacion.nombre) == nombre.lower()
        )
    )
    if current_id:
        query = query.filter(CentroRehabilitacion.id != current_id)

    centro_existente = query.first()

    if centro_existente:
        if centro_existente.identificacion.lower() == identificacion.lower():
            logger.warning(f"{LogMessages.CentroRehabilitacion.DUPLICATE_IDENTIFICACION} - ID: {current_id}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Un centro con esta identificación ya existe")
        elif centro_existente.nombre.lower() == nombre.lower():
            logger.warning(f"{LogMessages.CentroRehabilitacion.DUPLICATE_NOMBRE} - ID: {current_id}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Un centro con este nombre ya existe")


def create_centro(db: Session, centro: CentroRehabilitacionIn):
    logger.info(f"{LogMessages.CentroRehabilitacion.CREATE_ATTEMPT} - Identificación: {centro.identificacion}")
    try:
        _check_centro_constraints(db, centro.identificacion, centro.nombre)

        nuevo = CentroRehabilitacion(
            id_tipo_identificacion=centro.id_tipo_identificacion,
            identificacion=centro.identificacion,
            nombre=centro.nombre,
            correo=centro.correo
        )
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        logger.info(f"{LogMessages.CentroRehabilitacion.CREATE_SUCCESS} - ID: {nuevo.id}")
        return nuevo
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.CentroRehabilitacion.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear centro")


def get_centros(db: Session):
    logger.info(LogMessages.CentroRehabilitacion.FETCH_ALL)
    try:
        return db.query(CentroRehabilitacion).all()
    except Exception as e:
        logger.error(f"{LogMessages.CentroRehabilitacion.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al listar centros")


def get_centro_by_id(db: Session, centro_id: UUID):
    logger.info(f"{LogMessages.CentroRehabilitacion.FETCH_BY_ID} - ID: {centro_id}")
    try:
        centro = db.query(CentroRehabilitacion).filter(CentroRehabilitacion.id == centro_id).first()
        if not centro:
            logger.warning(f"{LogMessages.CentroRehabilitacion.NOT_FOUND} - ID: {centro_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro no encontrado")
        return centro
    except Exception as e:
        logger.error(f"{LogMessages.CentroRehabilitacion.FETCH_BY_ID_FAIL} - ID: {centro_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al buscar centro")


def update_centro(db: Session, centro_id: UUID, centro_data: CentroRehabilitacionUpdate):
    logger.info(f"{LogMessages.CentroRehabilitacion.UPDATE_ATTEMPT} - ID: {centro_id}")
    try:
        if centro_data.identificacion and centro_data.nombre:
            _check_centro_constraints(db, centro_data.identificacion, centro_data.nombre, centro_id)
        elif centro_data.identificacion:
            _check_centro_constraints(db, centro_data.identificacion, "", centro_id)
        elif centro_data.nombre:
            _check_centro_constraints(db, "", centro_data.nombre, centro_id)

        centro = db.query(CentroRehabilitacion).filter(CentroRehabilitacion.id == centro_id).first()
        if not centro:
            logger.warning(f"{LogMessages.CentroRehabilitacion.NOT_FOUND} - ID: {centro_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centro no encontrado")

        centro_data_dict = centro_data.dict(exclude_unset=True)
        for key, value in centro_data_dict.items():
            setattr(centro, key, value)

        db.commit()
        db.refresh(centro)

        logger.info(f"{LogMessages.CentroRehabilitacion.UPDATE_SUCCESS} - ID: {centro_id}")
        return centro
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.CentroRehabilitacion.UPDATE_FAIL} - ID: {centro_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar centro")


def delete_centro(db: Session, centro_id: UUID):
    logger.info(f"{LogMessages.CentroRehabilitacion.DELETE_ATTEMPT} - ID: {centro_id}")
    try:
        centro = get_centro_by_id(db, centro_id)
        db.delete(centro)
        db.commit()
        logger.info(f"{LogMessages.CentroRehabilitacion.DELETE_SUCCESS} - ID: {centro_id}")
        return centro
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.CentroRehabilitacion.DELETE_FAIL} - ID: {centro_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar centro")
