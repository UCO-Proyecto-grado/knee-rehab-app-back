from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_entidades_primarias.schemas.estado_schema import EstadoCreate, EstadoOut
from lambda_entidades_primarias.services import estado_service
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

router = APIRouter(tags=["Estados"])

@router.post("/", response_model=EstadoOut)
def crear_estado(estado: EstadoCreate, db: Session = Depends(get_db)):
    try:
        nuevo = estado_service.create_estado(db, estado.nombre)
        data = EstadoOut.model_validate(nuevo).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Estado creado correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al crear estado", str(e))

@router.get("/", response_model=List[EstadoOut])
def listar_estados(db: Session = Depends(get_db)):
    try:
        estados = estado_service.get_estados(db)
        data = [EstadoOut.model_validate(e).model_dump(mode="json") for e in estados]
        return success_response(HTTP_200_OK, "Estados listados", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar estados", str(e))

@router.get("/{estado_id}", response_model=EstadoOut)
def obtener_estado(estado_id: UUID, db: Session = Depends(get_db)):
    try:
        estado = estado_service.get_estado_by_id(db, estado_id)
        if not estado:
            return error_response(HTTP_404_NOT_FOUND, "Estado no encontrado", "ID inválido o no existe")
        data = EstadoOut.model_validate(estado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar estado", str(e))

@router.put("/{estado_id}", response_model=EstadoOut)
def actualizar_estado(estado_id: UUID, estado: EstadoCreate, db: Session = Depends(get_db)):
    try:
        actualizado = estado_service.update_estado(db, estado_id, estado.nombre)
        data = EstadoOut.model_validate(actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Estado actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar estado", str(e))

@router.delete("/{estado_id}")
def eliminar_estado(estado_id: UUID, db: Session = Depends(get_db)):
    try:
        eliminado = estado_service.delete_estado(db, estado_id)
        return success_response(HTTP_200_OK, "Estado eliminado", {"id": str(estado_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar estado", str(e))
