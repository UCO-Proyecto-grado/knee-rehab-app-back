from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from instituciones.app.schemas.sede_schema import SedeCreate, SedeUpdate, SedeOut
from instituciones.app.services import sede_service as service
from instituciones.app.shared.db.dependencies import get_db
from instituciones.app.shared.core.response_handler import success_response, error_response
from instituciones.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from uuid import UUID

router = APIRouter(prefix="/sede")

@router.post("", response_model=SedeOut)
def crear_sede(sede_data: SedeCreate, db: Session = Depends(get_db)):
    try:
        sede = service.create_sede(db, sede_data)
        return success_response(HTTP_201_CREATED, "Sede creada correctamente", SedeOut.model_validate(sede).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear sede", str(e))

@router.get("", response_model=list[SedeOut])
def listar_sedes(db: Session = Depends(get_db)):
    try:
        sedes = service.get_sedes(db)
        return success_response(HTTP_200_OK, "Consulta exitosa", [SedeOut.model_validate(sede).model_dump(mode="json") for sede in sedes]   )
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar sedes", str(e))

@router.get("/{sede_id}", response_model=SedeOut)
def obtener_sede(sede_id: UUID, db: Session = Depends(get_db)):
    try:
        sede = service.get_sede_by_id(db, sede_id)
        if not sede:
            return error_response(HTTP_404_NOT_FOUND, "Sede no encontrada", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Consulta exitosa", SedeOut.model_validate(sede).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener sede", str(e))

@router.put("/{sede_id}", response_model=SedeOut)
def actualizar_sede(sede_id: UUID, sede_data: SedeUpdate, db: Session = Depends(get_db)):
    try:
        sede = service.update_sede(db, sede_id, sede_data)
        if not sede:
            return error_response(HTTP_404_NOT_FOUND, "Sede no encontrada", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Sede actualizada correctamente", SedeOut.model_validate(sede).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar sede", str(e))

@router.delete("/{sede_id}")
def eliminar_sede(sede_id: UUID, db: Session = Depends(get_db)):
    try:
        sede = service.delete_sede(db, sede_id)
        if not sede:
            return error_response(HTTP_404_NOT_FOUND, "Sede no encontrada", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Sede eliminada exitosamente", {"id": str(sede_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar sede", str(e))
