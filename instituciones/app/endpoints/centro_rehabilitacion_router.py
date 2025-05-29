from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from instituciones.app.schemas.instituciones.centro_rehabilitacion_schema import (
    CentroRehabilitacionCreate,
    CentroRehabilitacionUpdate,
    CentroRehabilitacionOut,
)
from instituciones.app.services import centro_rehabilitacion_service as service
from instituciones.app.models.instituciones.centro_rehabilitacion_model import CentroRehabilitacion
from instituciones.app.shared.db.dependencies import get_db
from instituciones.app.shared.core.response_handler import success_response, error_response
from instituciones.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

router = APIRouter(prefix="/centro-rehabilitacion")

@router.post("", response_model=CentroRehabilitacionOut)
def crear_centro(centro_data: CentroRehabilitacionCreate, db: Session = Depends(get_db)):
    try:
        centro = service.create_centro(db, CentroRehabilitacion(**centro_data.dict()))
        centro_out = CentroRehabilitacionOut.model_validate(centro)
        return success_response(HTTP_201_CREATED, "Centro de rehabilitacion creado con éxito", centro_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al crear un nuevo centro de rehabilitacion", str(e))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear centro", str(e))

@router.get("", response_model=List[CentroRehabilitacionOut])
def listar_centros(db: Session = Depends(get_db)):
    try:
        centros = service.get_centros(db)
        centros_out = [CentroRehabilitacionOut.model_validate(c).model_dump(mode="json") for c in centros]
        return success_response(HTTP_200_OK, "Consulta exitosa", centros_out)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar centros", str(e))

@router.get("/{centro_id}", response_model=CentroRehabilitacionOut)
def obtener_centro(centro_id: UUID, db: Session = Depends(get_db)):
    try:
        centro = service.get_centro_by_id(db, centro_id)
        if not centro:
            return error_response(HTTP_404_NOT_FOUND, "Centro no encontrado", "ID inválido o no existe")
        centro_out = CentroRehabilitacionOut.model_validate(centro)
        return success_response(HTTP_200_OK, "Consulta exitosa", centro_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al obtener centro", str(e))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener centro", str(e))

@router.put("/{centro_id}", response_model=CentroRehabilitacionOut)
def actualizar_centro(centro_id: UUID, centro_data: CentroRehabilitacionUpdate, db: Session = Depends(get_db)):
    try:
        centro_actualizado = service.update_centro(db, centro_id, centro_data)
        if not centro_actualizado:
            return error_response(HTTP_404_NOT_FOUND, "Centro de rehabilitacion no encontrado", "ID inválido o no existe")
        centro_out = CentroRehabilitacionOut.model_validate(centro_actualizado)
        return success_response(HTTP_200_OK, "Centro actualizado correctamente", centro_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al actualizar centro", str(e))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar centro", str(e))

@router.delete("/{centro_id}")
def eliminar_centro(centro_id: UUID, db: Session = Depends(get_db)):
    try:
        eliminado = service.delete_centro(db, centro_id)
        if not eliminado:
            return error_response(HTTP_404_NOT_FOUND, "Centro no encontrado", "ID inválido o no existe")
        return success_response(HTTP_200_OK, "Centro eliminado exitosamente", {"id": str(centro_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar centro", str(e))
