from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from terapias.app.schemas.terapias.plan_rehabilitacion_schema import (
    PlanRehabilitacionCreate,
    PlanRehabilitacionUpdate,
    PlanRehabilitacionOut
)
from terapias.app.services import plan_rehabilitacion_service as service
from terapias.app.shared.db.dependencies import get_db
from terapias.app.shared.core.response_handler import success_response, error_response
from terapias.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

router = APIRouter(prefix="/plan-rehabilitacion")


@router.post("", response_model=PlanRehabilitacionOut)
def crear_plan(data: PlanRehabilitacionCreate, db: Session = Depends(get_db)):
    try:
        plan = service.create_plan(db, data)
        return success_response(
            HTTP_201_CREATED,
            "Plan creado correctamente",
            PlanRehabilitacionOut.model_validate(plan).model_dump(mode="json")
        )
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear plan", str(e))


@router.get("", response_model=list[PlanRehabilitacionOut])
def listar_planes(db: Session = Depends(get_db)):
    try:
        planes = service.get_all_plans(db)
        return success_response(
            HTTP_200_OK,
            "Consulta exitosa",
            [PlanRehabilitacionOut.model_validate(p).model_dump(mode="json") for p in planes]
        )
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar planes", str(e))


@router.get("/{plan_id}", response_model=PlanRehabilitacionOut)
def obtener_plan(plan_id: UUID, db: Session = Depends(get_db)):
    try:
        plan = service.get_plan_by_id(db, plan_id)
        if not plan:
            return error_response(HTTP_404_NOT_FOUND, "Plan no encontrado", "ID inválido o no existe")
        return success_response(
            HTTP_200_OK,
            "Consulta exitosa",
            PlanRehabilitacionOut.model_validate(plan).model_dump(mode="json")
        )
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener plan", str(e))


@router.put("/{plan_id}", response_model=PlanRehabilitacionOut)
def actualizar_plan(plan_id: UUID, data: PlanRehabilitacionUpdate, db: Session = Depends(get_db)):
    try:
        plan = service.update_plan(db, plan_id, data)
        if not plan:
            return error_response(HTTP_404_NOT_FOUND, "Plan no encontrado", "ID inválido o no existe")
        return success_response(
            HTTP_200_OK,
            "Plan actualizado correctamente",
            PlanRehabilitacionOut.model_validate(plan).model_dump(mode="json")
        )
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar plan", str(e))


@router.delete("/{plan_id}")
def eliminar_plan(plan_id: UUID, db: Session = Depends(get_db)):
    try:
        plan = service.delete_plan(db, plan_id)
        if not plan:
            return error_response(HTTP_404_NOT_FOUND, "Plan no encontrado", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Plan eliminado correctamente", {"id": str(plan_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar plan", str(e))
