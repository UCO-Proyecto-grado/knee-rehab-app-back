from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from recursos_terapeuticos.app.schemas.recursos_terapeuticos.modulo_schema import ModuloCreate, ModuloUpdate, ModuloOut
from recursos_terapeuticos.app.services.modulo_service import create_modulo, get_modulos, get_modulo_by_id, update_modulo, delete_modulo
from recursos_terapeuticos.app.shared.db.dependencies import get_db
from recursos_terapeuticos.app.shared.core.response_handler import success_response, error_response
from recursos_terapeuticos.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

router = APIRouter(prefix="/modulos")

@router.post("", response_model=ModuloOut)
def crear_modulo(modulo: ModuloCreate, db: Session = Depends(get_db)):
    try:
        modulo_out = create_modulo(db, modulo)
        return success_response(HTTP_201_CREATED, "Modulo creado con éxito", modulo_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al crear modulo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear modulo", str(e))

@router.get("", response_model=List[ModuloOut])
def listar_modulos(id_centro: UUID, db: Session = Depends(get_db)):
    try:
        modulos = get_modulos(db, id_centro)
        return success_response(HTTP_200_OK, "Modulos listados con éxito", [modulo.model_dump(mode="json") for modulo in modulos])
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al listar modulos", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar modulos", str(e))

@router.get("/{id_modulo}", response_model=ModuloOut)
def obtener_modulo(id_modulo: UUID, db: Session = Depends(get_db)):
    try:
        modulo = get_modulo_by_id(db, id_modulo)
        return success_response(HTTP_200_OK, "Modulo obtenido con éxito", modulo.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al obtener modulo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener modulo", str(e))

@router.put("/{id_modulo}", response_model=ModuloOut)
def actualizar_modulo(id_modulo: UUID, modulo: ModuloUpdate, db: Session = Depends(get_db)):
    try:
        modulo_out = update_modulo(db, id_modulo, modulo)
        return success_response(HTTP_200_OK, "Modulo actualizado con éxito", modulo_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al actualizar modulo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar modulo", str(e))

@router.delete("/{id_modulo}")
def eliminar_modulo(id_modulo: UUID, db: Session = Depends(get_db)):
    try:
        delete_modulo(db, id_modulo)
        return success_response(HTTP_200_OK, "Modulo eliminado con éxito")
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al eliminar modulo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar modulo", str(e))
