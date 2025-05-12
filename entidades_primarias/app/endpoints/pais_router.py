from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from entidades_primarias.app.services import pais_service
from entidades_primarias.app.schemas.pais_schema import PaisCreate, PaisUpdate, PaisOut
from entidades_primarias.app.shared.db.dependencies import get_db
from entidades_primarias.app.shared.core.response_handler import success_response, error_response
from entidades_primarias.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

router = APIRouter(prefix="/paises")

@router.post("", response_model=PaisOut)
def crear_pais(pais: PaisCreate, db: Session = Depends(get_db)):
    try:
        nuevo_pais = pais_service.create_pais(db, pais.nombre)
        data = PaisOut.model_validate(nuevo_pais).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "País creado correctamente", data)
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Nombre de país duplicado", str(e))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))

@router.get("", response_model=List[PaisOut])
def listar_paises(db: Session = Depends(get_db)):
    try:
        paises = pais_service.get_paises(db)
        data = [PaisOut.model_validate(p).model_dump(mode="json") for p in paises]
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))

@router.get("/{pais_id}", response_model=PaisOut)
def obtener_pais(pais_id: UUID, db: Session = Depends(get_db)):
    try:
        pais = pais_service.get_pais_by_id(db, pais_id)
        if not pais:
            return error_response(HTTP_404_NOT_FOUND, "País no encontrado", "ID inválido o no existe")
        data = PaisOut.model_validate(pais).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))

@router.put("/{pais_id}", response_model=PaisOut)
def actualizar_pais(pais_id: UUID, pais: PaisUpdate, db: Session = Depends(get_db)):
    try:
        pais_actualizado = pais_service.update_pais(db, pais_id, pais.nombre)
        if not pais_actualizado:
            return error_response(HTTP_404_NOT_FOUND, "País no encontrado", "ID inválido o no existe")
        data = PaisOut.model_validate(pais_actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "País actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))

@router.delete("/{pais_id}")
def eliminar_pais(pais_id: UUID, db: Session = Depends(get_db)):
    try:
        pais_eliminado = pais_service.delete_pais(db, pais_id)
        if not pais_eliminado:
            return error_response(HTTP_404_NOT_FOUND, "País no encontrado", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "País eliminado exitosamente", {"id": str(pais_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))