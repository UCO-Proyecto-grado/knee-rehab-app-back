from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from terapias.app.schemas.terapias.estado_plan_rehabilitacion_ejercicio_schema import (
    EstadoPRECreate, EstadoPREUpdate, EstadoPREOut
)
from terapias.app.services import estado_plan_rehabilitacion_ejercicio_service as service
from terapias.app.shared.db.dependencies import get_db
from terapias.app.shared.core.response_handler import success_response, error_response
from terapias.app.shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter("/estado-plan-ejercicio")


@router.post("", response_model=EstadoPREOut)
def crear(data: EstadoPRECreate, db: Session = Depends(get_db)):
    try:
        estado = service.create_estado(db, data)
        return success_response(HTTP_201_CREATED, "Estado creado correctamente", EstadoPREOut.model_validate(estado).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear estado", str(e))


@router.get("", response_model=list[EstadoPREOut])
def listar(db: Session = Depends(get_db)):
    try:
        estados = service.get_all_estados(db)
        return success_response(HTTP_200_OK, "Consulta exitosa", [EstadoPREOut.model_validate(e).model_dump(mode="json") for e in estados])
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar", str(e))


@router.get("/{estado_id}", response_model=EstadoPREOut)
def obtener(estado_id: UUID, db: Session = Depends(get_db)):
    try:
        estado = service.get_estado_by_id(db, estado_id)
        if not estado:
            return error_response(HTTP_404_NOT_FOUND, "Estado no encontrado", "ID inválido")
        return success_response(HTTP_200_OK, "Consulta exitosa", EstadoPREOut.model_validate(estado).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar estado", str(e))


@router.put("/{estado_id}", response_model=EstadoPREOut)
def actualizar(estado_id: UUID, data: EstadoPREUpdate, db: Session = Depends(get_db)):
    try:
        estado = service.update_estado(db, estado_id, data)
        if not estado:
            return error_response(HTTP_404_NOT_FOUND, "Estado no encontrado", "ID inválido")
        return success_response(HTTP_200_OK, "Actualización exitosa", EstadoPREOut.model_validate(estado).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar estado", str(e))


@router.delete("/{estado_id}")
def eliminar(estado_id: UUID, db: Session = Depends(get_db)):
    try:
        estado = service.delete_estado(db, estado_id)
        if not estado:
            return error_response(HTTP_404_NOT_FOUND, "Estado no encontrado", "ID inválido")
        return success_response(HTTP_200_OK, "Eliminado correctamente", {"id": str(estado_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar estado", str(e))
