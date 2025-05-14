from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from instituciones.app.shared.db.dependencies import get_db
from instituciones.app.schemas.instituciones.fisioterapeuta_sede_schema import FisioterapeutaSedeCreate, FisioterapeutaSedeOut
from instituciones.app.services import fisioterapeuta_sede_service as service
from instituciones.app.shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR    
from instituciones.app.shared.core.response_handler import success_response, error_response
router = APIRouter(prefix="/fisioterapeuta-sede")

@router.post("/{id_fisioterapeuta}/{id_sede}")
def crear_fisioterapeuta_sede(id_fisioterapeuta: UUID, id_sede: UUID, db: Session = Depends(get_db)):
    try:
        relacion = service.create_fisioterapeuta_sede(db, id_fisioterapeuta, id_sede)
        if not relacion:
            return error_response(HTTP_404_NOT_FOUND, "La relación ya existe", "Duplicado")
        return success_response(HTTP_201_CREATED, "Relación creada correctamente", FisioterapeutaSedeOut.model_validate(relacion).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear relación", str(e))


@router.get("/{id_fisioterapeuta}", response_model=List[FisioterapeutaSedeOut])
def listar_fisioterapeuta_sede(id_fisioterapeuta: UUID, db: Session = Depends(get_db)):
    try:
        relaciones = service.get_fisioterapeuta_sede(db, id_fisioterapeuta)
        return success_response(HTTP_200_OK, "Consulta exitosa", [FisioterapeutaSedeOut.model_validate(r).model_dump(mode="json") for r in relaciones])
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar relaciones", str(e))

@router.delete("/{id_fisioterapeuta_sede}")
def eliminar_fisioterapeuta_sede(id_fisioterapeuta_sede: UUID, db: Session = Depends(get_db)):
    try:
        relacion = service.delete_fisioterapeuta_sede(db, id_fisioterapeuta_sede)
        return success_response(HTTP_200_OK, "Relación eliminada correctamente", FisioterapeutaSedeOut.model_validate(relacion).model_dump(mode="json"))
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar relación", str(e))