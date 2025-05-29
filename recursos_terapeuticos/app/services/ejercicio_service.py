from recursos_terapeuticos.app.shared.db.base import Ejercicio
from recursos_terapeuticos.app.shared.db.base import Modulo
from recursos_terapeuticos.app.schemas.recursos_terapeuticos.ejercicio_schema import EjercicioCreate, EjercicioUpdate, EjercicioOut
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status
from uuid import UUID
from recursos_terapeuticos.app.shared.utils.logging_config import get_logger
from recursos_terapeuticos.app.shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def get_ejercicio(db: Session, id_modulo: UUID):
    logger.info(f"{LogMessages.Ejercicio.FETCH_ALL} - Módulo ID: {id_modulo}")
    try:
        ejercicios = db.query(Ejercicio).filter(Ejercicio.id_modulo == id_modulo).all()
        return [EjercicioOut.model_validate(e) for e in ejercicios]
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al listar ejercicios")


def get_ejercicio_by_id(db: Session, id_ejercicio: UUID) -> EjercicioOut:
    logger.info(f"{LogMessages.Ejercicio.FETCH_BY_ID} - ID: {id_ejercicio}")
    try:
        ejercicio = db.query(Ejercicio).filter(Ejercicio.id == id_ejercicio).first()
        if not ejercicio:
            logger.warning(f"{LogMessages.Ejercicio.NOT_FOUND} - ID: {id_ejercicio}")
            raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
        return EjercicioOut.model_validate(ejercicio)
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.FETCH_BY_ID_FAIL} - ID: {id_ejercicio} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno al buscar ejercicio")


def create_ejercicio(db: Session, ejercicio: EjercicioCreate) -> EjercicioOut:
    logger.info(f"{LogMessages.Ejercicio.CREATE_ATTEMPT} - Nombre: {ejercicio.nombre}")
    try:
        db_ejercicio = Ejercicio(**ejercicio.model_dump())
        db.add(db_ejercicio)
        db.commit()
        db.refresh(db_ejercicio)
        logger.info(f"{LogMessages.Ejercicio.CREATE_SUCCESS} - ID: {db_ejercicio.id}")
        return EjercicioOut.model_validate(db_ejercicio)
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno al crear ejercicio")


def update_ejercicio(db: Session, id_ejercicio: UUID, ejercicio: EjercicioUpdate) -> EjercicioOut:
    logger.info(f"{LogMessages.Ejercicio.UPDATE_ATTEMPT} - ID: {id_ejercicio}")
    try:
        db_ejercicio = db.query(Ejercicio).filter(Ejercicio.id == id_ejercicio).first()
        if not db_ejercicio:
            logger.warning(f"{LogMessages.Ejercicio.NOT_FOUND} - ID: {id_ejercicio}")
            raise HTTPException(status_code=404, detail="Ejercicio no encontrado")

        for key, value in ejercicio.model_dump(exclude_unset=True).items():
            setattr(db_ejercicio, key, value)

        db.commit()
        db.refresh(db_ejercicio)

        logger.info(f"{LogMessages.Ejercicio.UPDATE_SUCCESS} - ID: {id_ejercicio}")
        return EjercicioOut.model_validate(db_ejercicio)
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.UPDATE_FAIL} - ID: {id_ejercicio} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno al actualizar ejercicio")


def delete_ejercicio(db: Session, id_ejercicio: UUID):
    logger.info(f"{LogMessages.Ejercicio.DELETE_ATTEMPT} - ID: {id_ejercicio}")
    try:
        ejercicio = db.query(Ejercicio).filter(Ejercicio.id == id_ejercicio).first()
        if not ejercicio:
            logger.warning(f"{LogMessages.Ejercicio.NOT_FOUND} - ID: {id_ejercicio}")
            raise HTTPException(status_code=404, detail="Ejercicio no encontrado")
        db.delete(ejercicio)
        db.commit()
        logger.info(f"{LogMessages.Ejercicio.DELETE_SUCCESS} - ID: {id_ejercicio}")
        return {"message": "Ejercicio eliminado correctamente"}
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.DELETE_FAIL} - ID: {id_ejercicio} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno al eliminar ejercicio")


def get_ejercicio_por_centro_rehabilitacion(db: Session, id_centro_rehabilitacion: UUID) -> list[EjercicioOut]:
    logger.info(f"{LogMessages.Ejercicio.FETCH_BY_CENTRO} - Centro ID: {id_centro_rehabilitacion}")
    try:
        ejercicios = (
            db.query(Ejercicio)
            .join(Ejercicio.modulo)
            .filter(Modulo.id_centro_rehabilitacion == id_centro_rehabilitacion)
            .options(selectinload(Ejercicio.modulo))
            .all()
        )
        return [EjercicioOut.model_validate(e) for e in ejercicios]
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.FETCH_BY_CENTRO_FAIL} - Centro ID: {id_centro_rehabilitacion} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar ejercicios por centro")


def get_ejercicio_por_centro_rehabilitacion_y_modulo(db: Session, id_centro_rehabilitacion: UUID, id_modulo: UUID) -> list[EjercicioOut]:
    logger.info(f"{LogMessages.Ejercicio.FETCH_BY_CENTRO_Y_MODULO} - Centro ID: {id_centro_rehabilitacion}, Módulo ID: {id_modulo}")
    try:
        ejercicios = (
            db.query(Ejercicio)
            .join(Ejercicio.modulo)
            .filter(Modulo.id_centro_rehabilitacion == id_centro_rehabilitacion, Ejercicio.id_modulo == id_modulo)
            .options(selectinload(Ejercicio.modulo))
            .all()
        )
        return [EjercicioOut.model_validate(e) for e in ejercicios]
    except Exception as e:
        logger.error(f"{LogMessages.Ejercicio.FETCH_BY_CENTRO_Y_MODULO_FAIL} - Centro ID: {id_centro_rehabilitacion}, Módulo ID: {id_modulo} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar ejercicios por centro y módulo")
