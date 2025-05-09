from sqlalchemy.orm import Session
from uuid import UUID
from lambda_lesiones.models.categoria_tipo_lesion_model import CategoriaTipoLesion
from lambda_lesiones.schemas.categoria_tipo_lesion_schema import CategoriaTipoLesionCreate
from fastapi import HTTPException, status
from shared.utils.logging_config import get_logger
from shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def create_relacion(db: Session, data: CategoriaTipoLesionCreate):
    logger.info(f"{LogMessages.CategoriaTipoLesion.CREATE_ATTEMPT} - Categoría: {data.id_categoria}, Lesión: {data.id_lesion}")
    try:
        existe = db.query(CategoriaTipoLesion).filter_by(
            id_categoria=data.id_categoria,
            id_lesion=data.id_lesion
        ).first()

        if existe:
            logger.warning(f"{LogMessages.CategoriaTipoLesion.DUPLICATE} - Categoría: {data.id_categoria}, Lesión: {data.id_lesion}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La relación ya existe")

        nueva_relacion = CategoriaTipoLesion(**data.model_dump())
        db.add(nueva_relacion)
        db.commit()
        db.refresh(nueva_relacion)

        logger.info(f"{LogMessages.CategoriaTipoLesion.CREATE_SUCCESS} - ID: {nueva_relacion.id}")
        return nueva_relacion
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.CategoriaTipoLesion.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear relación")


def get_relaciones(db: Session):
    logger.info(LogMessages.CategoriaTipoLesion.FETCH_ALL)
    try:
        return db.query(CategoriaTipoLesion).all()
    except Exception as e:
        logger.error(f"{LogMessages.CategoriaTipoLesion.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al listar relaciones")


def delete_relacion(db: Session, id_relacion: UUID):
    logger.info(f"{LogMessages.CategoriaTipoLesion.DELETE_ATTEMPT} - ID: {id_relacion}")
    try:
        relacion = db.query(CategoriaTipoLesion).filter_by(id=id_relacion).first()
        if not relacion:
            logger.warning(f"{LogMessages.CategoriaTipoLesion.NOT_FOUND} - ID: {id_relacion}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relación no encontrada")

        db.delete(relacion)
        db.commit()

        logger.info(f"{LogMessages.CategoriaTipoLesion.DELETE_SUCCESS} - ID: {id_relacion}")
        return relacion
    except Exception as e:
        logger.error(f"{LogMessages.CategoriaTipoLesion.DELETE_FAIL} - ID: {id_relacion} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar relación")
