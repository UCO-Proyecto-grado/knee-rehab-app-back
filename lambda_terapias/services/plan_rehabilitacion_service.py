from sqlalchemy.orm import Session
from uuid import UUID
from lambda_terapias.models.plan_rehabilitacion_model import PlanRehabilitacion
from lambda_terapias.schemas.plan_rehabilitacion_schema import (
    PlanRehabilitacionCreate,
    PlanRehabilitacionUpdate
)


def create_plan(db: Session, data: PlanRehabilitacionCreate):
    plan = PlanRehabilitacion(**data.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


def get_all_plans(db: Session):
    return db.query(PlanRehabilitacion).all()


def get_plan_by_id(db: Session, plan_id: UUID):
    return db.query(PlanRehabilitacion).filter(PlanRehabilitacion.id == plan_id).first()


def update_plan(db: Session, plan_id: UUID, data: PlanRehabilitacionUpdate):
    plan = get_plan_by_id(db, plan_id)
    if not plan:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(plan, key, value)
    db.commit()
    db.refresh(plan)
    return plan


def delete_plan(db: Session, plan_id: UUID):
    plan = get_plan_by_id(db, plan_id)
    if plan:
        db.delete(plan)
        db.commit()
    return plan
