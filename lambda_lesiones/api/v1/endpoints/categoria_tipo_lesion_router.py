from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from lambda_lesiones.schemas.categoria_tipo_lesion_schema import (
    CategoriaTipoLesionCreate, CategoriaTipoLesionOut
)
from lambda_lesiones.services import categoria_tipo_lesion_service as service
from shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from uuid import UUID

router = APIRouter(prefix="/categoria-tipo-lesion", tags=["CategoriaTipoLesion"])


@router.post("", response_model=CategoriaTipoLesionOut)
def crear_relacion(data: CategoriaTipoLesionCreate, db: Session = Depends(get_db)):
    try:
        relacion = service.create_relacion(db, data)
        if not relacion:
            return error_response(HTTP_404_NOT_FOUND, "La relación ya existe", "Duplicado")
        return success_response(HTTP_201_CREATED, "Relación creada correctamente", CategoriaTipoLesionOut.model_validate(relacion).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear relación", str(e))


@router.get("", response_model=list[CategoriaTipoLesionOut])
def listar_relaciones(db: Session = Depends(get_db)):
    try:
        relaciones = service.get_relaciones(db)
        return success_response(HTTP_200_OK, "Consulta exitosa", [CategoriaTipoLesionOut.model_validate(r).model_dump(mode="json") for r in relaciones])
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar relaciones", str(e))


@router.delete("/{id_relacion}")
def eliminar_relacion(id_relacion: UUID, db: Session = Depends(get_db)):
    try:
        relacion = service.delete_relacion(db, id_relacion)
        if not relacion:
            return error_response(HTTP_404_NOT_FOUND, "Relación no encontrada", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Relación eliminada correctamente", {"id": str(id_relacion)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar relación", str(e))
