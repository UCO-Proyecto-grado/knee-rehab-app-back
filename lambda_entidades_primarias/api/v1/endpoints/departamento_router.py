from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_entidades_primarias.services import departamento_service
from lambda_entidades_primarias.schemas.departamento_schema import DepartamentoCreate, DepartamentoOut
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

router = APIRouter()

@router.post("", response_model=DepartamentoOut)
def crear_departamento(departamento: DepartamentoCreate, db: Session = Depends(get_db)):
    try:
        nuevo = departamento_service.create_departamento(db, departamento.nombre, departamento.id_pais)
        data = DepartamentoOut.model_validate(nuevo).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Departamento creado correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear el departamento", str(e))

@router.get("", response_model=List[DepartamentoOut])
def listar_departamentos(db: Session = Depends(get_db)):
    try:
        items = departamento_service.get_departamentos(db)
        data = [DepartamentoOut.model_validate(dep).model_dump(mode="json") for dep in items]
        return success_response(HTTP_200_OK, "Departamentos listados exitosamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno al listar", str(e))

@router.get("/{departamento_id}", response_model=DepartamentoOut)
def obtener_departamento(departamento_id: UUID, db: Session = Depends(get_db)):
    try:
        dep = departamento_service.get_departamento_by_id(db, departamento_id)
        if not dep:
            return error_response(HTTP_404_NOT_FOUND, "Departamento no encontrado", "ID inválido o no existe")
        data = DepartamentoOut.model_validate(dep).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener el departamento", str(e))

@router.put("/{departamento_id}", response_model=DepartamentoOut)
def actualizar_departamento(departamento_id: UUID, departamento: DepartamentoCreate, db: Session = Depends(get_db)):
    try:
        actualizado = departamento_service.update_departamento(
            db, departamento_id, departamento.nombre, departamento.id_pais
        )
        if not actualizado:
            return error_response(HTTP_404_NOT_FOUND, "Departamento no encontrado", "ID inválido o no existe")
        data = DepartamentoOut.model_validate(actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Departamento actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar el departamento", str(e))

@router.delete("/{departamento_id}")
def eliminar_departamento(departamento_id: UUID, db: Session = Depends(get_db)):
    try:
        eliminado = departamento_service.delete_departamento(db, departamento_id)
        if not eliminado:
            return error_response(HTTP_404_NOT_FOUND, "Departamento no encontrado", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Departamento eliminado exitosamente", {"id": str(departamento_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar el departamento", str(e))
