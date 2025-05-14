from sqlalchemy.orm import Session
from uuid import UUID
from terapias.app.models.plan_rehabilitacion_model import PlanRehabilitacion
from terapias.app.schemas.plan_rehabilitacion_schema import PlanRehabilitacionCreate, PlanRehabilitacionUpdate
from fastapi import HTTPException, status
from terapias.app.shared.utils.logging_config import get_logger
from terapias.app.shared.utils.log_messages import LogMessages

logger = get_logger(__name__)


def create_plan(db: Session, data: PlanRehabilitacionCreate):
    logger.info(f"{LogMessages.PlanRehabilitacion.CREATE_ATTEMPT}")
    try:
        plan = PlanRehabilitacion(**data.model_dump())
        db.add(plan)
        db.commit()
        db.refresh(plan)
        logger.info(f"{LogMessages.PlanRehabilitacion.CREATE_SUCCESS} - ID: {plan.id}")
        return plan
    except Exception as e:
        logger.error(f"{LogMessages.PlanRehabilitacion.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al crear plan de rehabilitación")


def get_all_plans(db: Session):
    logger.info(LogMessages.PlanRehabilitacion.FETCH_ALL)
    try:
        return db.query(PlanRehabilitacion).all()
    except Exception as e:
        logger.error(f"{LogMessages.PlanRehabilitacion.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al listar planes de rehabilitación")


def get_plan_by_id(db: Session, plan_id: UUID):
    logger.info(f"{LogMessages.PlanRehabilitacion.FETCH_BY_ID} - ID: {plan_id}")
    try:
        plan = db.query(PlanRehabilitacion).filter(PlanRehabilitacion.id == plan_id).first()
        if not plan:
            logger.warning(f"{LogMessages.PlanRehabilitacion.NOT_FOUND} - ID: {plan_id}")
            raise HTTPException(status_code=404, detail="Plan de rehabilitación no encontrado")
        return plan
    except Exception as e:
        logger.error(f"{LogMessages.PlanRehabilitacion.FETCH_BY_ID_FAIL} - ID: {plan_id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al buscar plan de rehabilitación")


def update_plan(db: Session, plan_id: UUID, data: PlanRehabilitacionUpdate):
    logger.info(f"{LogMessages.PlanRehabilitacion.UPDATE_ATTEMPT} - ID: {plan_id}")
    try:
        plan = db.query(PlanRehabilitacion).filter_by(id=plan_id).first()
        if not plan:
            logger.warning(f"{LogMessages.PlanRehabilitacion.NOT_FOUND} - ID: {plan_id}")
            raise HTTPException(status_code=404, detail="Plan de rehabilitación no encontrado")

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(plan, key, value)

        db.commit()
        db.refresh(plan)

        logger.info(f"{LogMessages.PlanRehabilitacion.UPDATE_SUCCESS} - ID: {plan_id}")
        return plan
    except Exception as e:
        logger.error(f"{LogMessages.PlanRehabilitacion.UPDATE_FAIL} - ID: {plan_id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al actualizar plan de rehabilitación")


def delete_plan(db: Session, plan_id: UUID):
    logger.info(f"{LogMessages.PlanRehabilitacion.DELETE_ATTEMPT} - ID: {plan_id}")
    try:
        plan = db.query(PlanRehabilitacion).filter_by(id=plan_id).first()
        if not plan:
            logger.warning(f"{LogMessages.PlanRehabilitacion.NOT_FOUND} - ID: {plan_id}")
            raise HTTPException(status_code=404, detail="Plan de rehabilitación no encontrado")

        db.delete(plan)
        db.commit()

        logger.info(f"{LogMessages.PlanRehabilitacion.DELETE_SUCCESS} - ID: {plan_id}")
        return plan
    except Exception as e:
        logger.error(f"{LogMessages.PlanRehabilitacion.DELETE_FAIL} - ID: {plan_id} - Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al eliminar plan de rehabilitación")
