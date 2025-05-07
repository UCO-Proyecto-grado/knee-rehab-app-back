from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_acceso_personal.schemas.fisioterapeuta_schema import FisioterapeutaCreate, FisioterapeutaOut
from lambda_acceso_personal.services import fisioterapeuta_service
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter()

@router.post("", response_model=FisioterapeutaOut)
def crear_fisioterapeuta(fisioterapeuta: FisioterapeutaCreate, db: Session = Depends(get_db)):
    try:
        nuevo = fisioterapeuta_service.create_fisioterapeuta(db, fisioterapeuta.model_dump())
        data = FisioterapeutaOut.model_validate(nuevo).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Fisioterapeuta creado correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear el fisioterapeuta", str(e))

@router.get("", response_model=List[FisioterapeutaOut])
def listar_fisioterapeutas(db: Session = Depends(get_db)):
    try:
        items = fisioterapeuta_service.get_fisioterapeutas(db)
        data = [FisioterapeutaOut.model_validate(f).model_dump(mode="json") for f in items]
        return success_response(HTTP_200_OK, "Fisioterapeutas listados", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar fisioterapeutas", str(e))

@router.get("/{fisioterapeuta_id}", response_model=FisioterapeutaOut)
def obtener_fisioterapeuta(fisioterapeuta_id: UUID, db: Session = Depends(get_db)):
    try:
        f = fisioterapeuta_service.get_fisioterapeuta_by_id(db, fisioterapeuta_id)
        if not f:
            return error_response(HTTP_404_NOT_FOUND, "Fisioterapeuta no encontrado", "ID inválido o no existe")
        data = FisioterapeutaOut.model_validate(f).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar fisioterapeuta", str(e))

@router.put("/{fisioterapeuta_id}", response_model=FisioterapeutaOut)
def actualizar_fisioterapeuta(fisioterapeuta_id: UUID, fisioterapeuta: FisioterapeutaCreate, db: Session = Depends(get_db)):
    try:
        actualizado = fisioterapeuta_service.update_fisioterapeuta(db, fisioterapeuta_id, fisioterapeuta.model_dump())
        data = FisioterapeutaOut.model_validate(actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Fisioterapeuta actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar fisioterapeuta", str(e))

@router.delete("/{fisioterapeuta_id}")
def eliminar_fisioterapeuta(fisioterapeuta_id: UUID, db: Session = Depends(get_db)):
    try:
        fisioterapeuta_service.delete_fisioterapeuta(db, fisioterapeuta_id)
        return success_response(HTTP_200_OK, "Fisioterapeuta eliminado", {"id": str(fisioterapeuta_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar fisioterapeuta", str(e))
