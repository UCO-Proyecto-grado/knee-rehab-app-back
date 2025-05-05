from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_entidades_primarias.services import ciudad_service
from lambda_entidades_primarias.schemas.ciudad_schema import CiudadCreate, CiudadOut
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

router = APIRouter(tags=["Ciudades"])

@router.post("/", response_model=CiudadOut)
def crear_ciudad(ciudad: CiudadCreate, db: Session = Depends(get_db)):
    try:
        nueva = ciudad_service.create_ciudad(db, ciudad.nombre, ciudad.id_departamento)
        data = CiudadOut.model_validate(nueva).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Ciudad creada correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear la ciudad", str(e))

@router.get("/", response_model=List[CiudadOut])
def listar_ciudades(db: Session = Depends(get_db)):
    try:
        items = ciudad_service.get_ciudades(db)
        data = [CiudadOut.model_validate(c).model_dump(mode="json") for c in items]
        return success_response(HTTP_200_OK, "Ciudades listadas", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar ciudades", str(e))

@router.get("/{ciudad_id}", response_model=CiudadOut)
def obtener_ciudad(ciudad_id: UUID, db: Session = Depends(get_db)):
    try:
        c = ciudad_service.get_ciudad_by_id(db, ciudad_id)
        if not c:
            return error_response(HTTP_404_NOT_FOUND, "Ciudad no encontrada", "ID inválido o no existe")
        data = CiudadOut.model_validate(c).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar ciudad", str(e))

@router.put("/{ciudad_id}", response_model=CiudadOut)
def actualizar_ciudad(ciudad_id: UUID, ciudad: CiudadCreate, db: Session = Depends(get_db)):
    try:
        actualizada = ciudad_service.update_ciudad(db, ciudad_id, ciudad.nombre, ciudad.id_departamento)
        data = CiudadOut.model_validate(actualizada).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Ciudad actualizada correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar ciudad", str(e))

@router.delete("/{ciudad_id}")
def eliminar_ciudad(ciudad_id: UUID, db: Session = Depends(get_db)):
    try:
        eliminada = ciudad_service.delete_ciudad(db, ciudad_id)
        return success_response(HTTP_200_OK, "Ciudad eliminada", {"id": str(ciudad_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar ciudad", str(e))
