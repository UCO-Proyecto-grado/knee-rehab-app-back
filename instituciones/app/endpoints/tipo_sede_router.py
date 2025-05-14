from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from instituciones.app.services import tipo_sede_service
from instituciones.app.schemas.instituciones.tipo_sede_schema import TipoSedeCreate, TipoSedeOut, TipoSedeUpdate
from instituciones.app.shared.db.dependencies import get_db
from instituciones.app.shared.core.response_handler import success_response, error_response
from instituciones.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)
router = APIRouter(prefix="/tipo-sede")

@router.post("", response_model=TipoSedeOut)
def crear_tipo_sede(tipo_sede: TipoSedeCreate, db: Session = Depends(get_db)):
    try:
        nuevo_tipo_sede = tipo_sede_service.create_tipo_sede(db, tipo_sede.nombre)
        data = TipoSedeOut.model_validate(nuevo_tipo_sede).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Tipo de sede creado correctamente", data)
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Nombre de tipo de sede duplicado", str(e))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))

@router.get("", response_model=List[TipoSedeOut])
def listar_tipo_sedes(db: Session = Depends(get_db)):
    try:
        tipo_sedes = tipo_sede_service.get_tipo_sedes(db)
        data = [TipoSedeOut.model_validate(tipo_sede).model_dump(mode="json") for tipo_sede in tipo_sedes]
        return success_response(HTTP_200_OK, "Tipos de sede listados correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))
    
@router.get("/{tipo_sede_id}", response_model=TipoSedeOut)
def obtener_tipo_sede(tipo_sede_id: UUID, db: Session = Depends(get_db)):
    try:
        tipo_sede = tipo_sede_service.get_tipo_sede_by_id(db, tipo_sede_id)
        if not tipo_sede:
            return error_response(HTTP_404_NOT_FOUND, "Tipo de sede no encontrado", "Tipo de sede no encontrado")
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))
    
@router.put("/{tipo_sede_id}", response_model=TipoSedeOut)
def actualizar_tipo_sede(tipo_sede_id: UUID, tipo_sede: TipoSedeUpdate, db: Session = Depends(get_db)):
    try:
        tipo_sede_actualizada = tipo_sede_service.update_tipo_sede(db, tipo_sede_id, tipo_sede.nombre)
        data = TipoSedeOut.model_validate(tipo_sede_actualizada).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Tipo de sede actualizado correctamente", data)
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Nombre de tipo de sede duplicado", str(e))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))
    
@router.delete("/{tipo_sede_id}")
def eliminar_tipo_sede(tipo_sede_id: UUID, db: Session = Depends(get_db)):
    try:
        tipo_sede_eliminada = tipo_sede_service.delete_tipo_sede(db, tipo_sede_id)
        if not tipo_sede_eliminada:
            return error_response(HTTP_404_NOT_FOUND, "Tipo de sede no encontrado", "Tipo de sede no encontrado")
        return success_response(HTTP_200_OK, "Tipo de sede eliminado correctamente", None)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error interno del servidor", str(e))
