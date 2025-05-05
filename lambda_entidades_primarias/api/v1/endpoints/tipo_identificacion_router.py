from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_entidades_primarias.schemas.tipo_identificacion_schema import (
    TipoIdentificacionCreate, TipoIdentificacionOut
)
from lambda_entidades_primarias.services import tipo_identificacion_service
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

router = APIRouter(tags=["Tipos_dni"])

@router.post("/", response_model=TipoIdentificacionOut)
def crear_tipo(tipo: TipoIdentificacionCreate, db: Session = Depends(get_db)):
    try:
        nuevo = tipo_identificacion_service.create_tipo_identificacion(db, tipo.nombre, tipo.codigo)
        data = TipoIdentificacionOut.model_validate(nuevo).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Tipo de identificacion creado correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear el tipo de identificacion", str(e))

@router.get("/", response_model=List[TipoIdentificacionOut])
def listar_tipos(db: Session = Depends(get_db)):
    try:
        tipos = tipo_identificacion_service.get_tipos_identificacion(db)
        data = [TipoIdentificacionOut.model_validate(t).model_dump(mode="json") for t in tipos]
        return success_response(HTTP_200_OK, "Tipos de identificacion listados", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar", str(e))

@router.get("/{tipo_id}", response_model=TipoIdentificacionOut)
def obtener_tipo(tipo_id: UUID, db: Session = Depends(get_db)):
    try:
        tipo = tipo_identificacion_service.get_tipo_identificacion_by_id(db, tipo_id)
        if not tipo:
            return error_response(HTTP_404_NOT_FOUND, "Tipo de identificacion no encontrado", "ID inválido o no existe")
        data = TipoIdentificacionOut.model_validate(tipo).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar tipo de identificacion", str(e))

@router.put("/{tipo_id}", response_model=TipoIdentificacionOut)
def actualizar_tipo(tipo_id: UUID, tipo: TipoIdentificacionCreate, db: Session = Depends(get_db)):
    try:
        actualizado = tipo_identificacion_service.update_tipo_identificacion(
            db, tipo_id, tipo.nombre, tipo.codigo
        )
        data = TipoIdentificacionOut.model_validate(actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Tipo de identificacion actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar tipo de identificacion", str(e))

@router.delete("/{tipo_id}")
def eliminar_tipo(tipo_id: UUID, db: Session = Depends(get_db)):
    try:
        eliminado = tipo_identificacion_service.delete_tipo_identificacion(db, tipo_id)
        return success_response(HTTP_200_OK, "Tipo de identificacion eliminado", {"id": str(tipo_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar tipo de identificacion", str(e))
