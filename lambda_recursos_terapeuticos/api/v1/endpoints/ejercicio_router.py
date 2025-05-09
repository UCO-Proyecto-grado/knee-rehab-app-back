from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from lambda_recursos_terapeuticos.schemas.ejercicio_schema import EjercicioCreate, EjercicioUpdate, EjercicioOut
from lambda_recursos_terapeuticos.services.ejercicio_service import get_ejercicio, get_ejercicio_by_id, create_ejercicio, update_ejercicio, delete_ejercicio, get_ejercicio_por_centro_rehabilitacion
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from uuid import UUID
from typing import List

router = APIRouter()

@router.post("", response_model=EjercicioOut)
def crear_ejercicio(ejercicio: EjercicioCreate, db: Session = Depends(get_db)):
    try:
        ejercicio_out = create_ejercicio(db, ejercicio)
        return success_response(HTTP_201_CREATED, "Ejercicio creado con éxito", ejercicio_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al crear ejercicio", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear ejercicio", str(e))
    
@router.get("/por-modulo", response_model=List[EjercicioOut])
def listar_ejercicios(id_modulo: UUID, db: Session = Depends(get_db)):
    try:
        ejercicios = get_ejercicio(db, id_modulo)
        return success_response(HTTP_200_OK, "Ejercicios listados con éxito", [ejercicio.model_dump(mode="json") for ejercicio in ejercicios])
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al listar ejercicios", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar ejercicios", str(e))
    
@router.get("/por-centro", response_model=List[EjercicioOut])
def listar_ejercicios_por_centro_rehabilitacion(
    id_centro_rehabilitacion: UUID,
    db: Session = Depends(get_db)
):
    try:
        ejercicios = get_ejercicio_por_centro_rehabilitacion(db, id_centro_rehabilitacion)
        return success_response(
            HTTP_200_OK,
            "Ejercicios listados con éxito",
            [e.model_dump(mode="json") for e in ejercicios]
        )
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar ejercicios", str(e))


@router.get("/{id_ejercicio}", response_model=EjercicioOut)
def obtener_ejercicio(id_ejercicio: UUID, db: Session = Depends(get_db)):
    try:
        ejercicio = get_ejercicio_by_id(db, id_ejercicio)
        return success_response(HTTP_200_OK, "Ejercicio obtenido con éxito", ejercicio.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al obtener ejercicio", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener ejercicio", str(e))
    
@router.put("/{id_ejercicio}", response_model=EjercicioOut)
def actualizar_ejercicio(id_ejercicio: UUID, ejercicio: EjercicioUpdate, db: Session = Depends(get_db)):
    try:
        ejercicio_out = update_ejercicio(db, id_ejercicio, ejercicio)
        return success_response(HTTP_200_OK, "Ejercicio actualizado con éxito", ejercicio_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al actualizar ejercicio", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar ejercicio", str(e))
    
@router.delete("/{id_ejercicio}")
def eliminar_ejercicio(id_ejercicio: UUID, db: Session = Depends(get_db)):
    try:
        delete_ejercicio(db, id_ejercicio)
        return success_response(HTTP_200_OK, "Ejercicio eliminado con éxito")
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al eliminar ejercicio", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar ejercicio", str(e))
    
