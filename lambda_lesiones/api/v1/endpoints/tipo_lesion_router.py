from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_lesiones.schemas.tipo_lesion_schema import TipoLesionCreate, TipoLesionOut
from lambda_lesiones.services import tipo_lesion_service
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter(tags=["Tipos de Lesión"])

@router.post("", response_model=TipoLesionOut)
def crear_tipo_lesion(tipo: TipoLesionCreate, db: Session = Depends(get_db)):
    try:
        nuevo = tipo_lesion_service.create_tipo_lesion(db, tipo.model_dump())
        data = TipoLesionOut.model_validate(nuevo).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Tipo de lesión creado correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear el tipo de lesión", str(e))

@router.get("", response_model=List[TipoLesionOut])
def listar_tipos_lesion(db: Session = Depends(get_db)):
    try:
        items = tipo_lesion_service.get_tipos_lesion(db)
        data = [TipoLesionOut.model_validate(t).model_dump(mode="json") for t in items]
        return success_response(HTTP_200_OK, "Tipos de lesión listados", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar tipos de lesión", str(e))

@router.get("/{tipo_lesion_id}", response_model=TipoLesionOut)
def obtener_tipo_lesion(tipo_lesion_id: UUID, db: Session = Depends(get_db)):
    try:
        tipo = tipo_lesion_service.get_tipo_lesion_by_id(db, tipo_lesion_id)
        if not tipo:
            return error_response(HTTP_404_NOT_FOUND, "Tipo de lesión no encontrado", "ID inválido o no existe")
        data = TipoLesionOut.model_validate(tipo).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar tipo de lesión", str(e))

@router.put("/{tipo_lesion_id}", response_model=TipoLesionOut)
def actualizar_tipo_lesion(tipo_lesion_id: UUID, tipo: TipoLesionCreate, db: Session = Depends(get_db)):
    try:
        actualizado = tipo_lesion_service.update_tipo_lesion(db, tipo_lesion_id, tipo.model_dump())
        data = TipoLesionOut.model_validate(actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Tipo de lesión actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar tipo de lesión", str(e))

@router.delete("/{tipo_lesion_id}")
def eliminar_tipo_lesion(tipo_lesion_id: UUID, db: Session = Depends(get_db)):
    try:
        tipo_lesion_service.delete_tipo_lesion(db, tipo_lesion_id)
        return success_response(HTTP_200_OK, "Tipo de lesión eliminado", {"id": str(tipo_lesion_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar tipo de lesión", str(e))
