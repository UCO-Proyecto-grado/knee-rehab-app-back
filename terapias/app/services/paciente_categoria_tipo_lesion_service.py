from sqlalchemy.orm import Session
from uuid import UUID
from terapias.app.models.terapias.paciente_categoria_tipo_lesion_model import PacienteCategoriaTipoLesion
from terapias.app.schemas.terapias.paciente_categoria_tipo_lesion_schema import PacienteCategoriaTipoLesionCreate
from fastapi import HTTPException, status
from terapias.app.shared.utils.logging_config import get_logger
from terapias.app.shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def create_relacion(db: Session, data: PacienteCategoriaTipoLesionCreate):
    logger.info(f"{LogMessages.PacienteCategoriaTipoLesion.CREATE_ATTEMPT} - Paciente: {data.id_paciente}, CategoríaTipoLesion: {data.id_categoria_tipo_lesion}")
    try:
        existe = db.query(PacienteCategoriaTipoLesion).filter_by(
            id_paciente=data.id_paciente,
            id_categoria_tipo_lesion=data.id_categoria_tipo_lesion
        ).first()
        if existe:
            logger.warning(f"{LogMessages.PacienteCategoriaTipoLesion.DUPLICATE} - Ya existe la relación")
            raise HTTPException(status_code=400, detail="La relación ya existe")

        nueva = PacienteCategoriaTipoLesion(**data.model_dump())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)

        logger.info(f"{LogMessages.PacienteCategoriaTipoLesion.CREATE_SUCCESS} - ID: {nueva.id}")
        return nueva
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"{LogMessages.PacienteCategoriaTipoLesion.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al crear relación")


def get_all(db: Session):
    logger.info(LogMessages.PacienteCategoriaTipoLesion.FETCH_ALL)
    try:
        return db.query(PacienteCategoriaTipoLesion).all()
    except Exception as e:
        logger.error(f"{LogMessages.PacienteCategoriaTipoLesion.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar relaciones")


def delete_relacion(db: Session, relacion_id: UUID):
    logger.info(f"{LogMessages.PacienteCategoriaTipoLesion.DELETE_ATTEMPT} - ID: {relacion_id}")
    try:
        relacion = db.query(PacienteCategoriaTipoLesion).filter_by(id=relacion_id).first()
        if not relacion:
            logger.warning(f"{LogMessages.PacienteCategoriaTipoLesion.NOT_FOUND} - ID: {relacion_id}")
            raise HTTPException(status_code=404, detail="Relación no encontrada")

        db.delete(relacion)
        db.commit()

        logger.info(f"{LogMessages.PacienteCategoriaTipoLesion.DELETE_SUCCESS} - ID: {relacion_id}")
        return relacion
    except Exception as e:
        logger.error(f"{LogMessages.PacienteCategoriaTipoLesion.DELETE_FAIL} - ID: {relacion_id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al eliminar relación")
