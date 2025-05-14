from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from terapias.app.schemas.paciente_categoria_tipo_lesion_schema import (
    PacienteCategoriaTipoLesionCreate,
    PacienteCategoriaTipoLesionOut
)
from terapias.app.services import paciente_categoria_tipo_lesion_service as service
from terapias.app.shared.db.dependencies import get_db
from terapias.app.shared.core.response_handler import success_response, error_response
from terapias.app.shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter()


@router.post("", response_model=PacienteCategoriaTipoLesionOut)
def crear(data: PacienteCategoriaTipoLesionCreate, db: Session = Depends(get_db)):
    try:
        relacion = service.create_relacion(db, data)
        if not relacion:
            return error_response(HTTP_404_NOT_FOUND, "Ya existe esta relación", "Duplicado")
        return success_response(HTTP_201_CREATED, "Relación creada correctamente", PacienteCategoriaTipoLesionOut.model_validate(relacion).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear relación", str(e))


@router.get("", response_model=list[PacienteCategoriaTipoLesionOut])
def listar(db: Session = Depends(get_db)):
    try:
        relaciones = service.get_all(db)
        return success_response(HTTP_200_OK, "Consulta exitosa", [PacienteCategoriaTipoLesionOut.model_validate(r).model_dump(mode="json") for r in relaciones])
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar relaciones", str(e))


@router.delete("/{relacion_id}")
def eliminar(relacion_id: UUID, db: Session = Depends(get_db)):
    try:
        relacion = service.delete_relacion(db, relacion_id)
        if not relacion:
            return error_response(HTTP_404_NOT_FOUND, "Relación no encontrada", "ID inválido o inexistente")
        return success_response(HTTP_200_OK, "Relación eliminada correctamente", {"id": str(relacion_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar relación", str(e))
