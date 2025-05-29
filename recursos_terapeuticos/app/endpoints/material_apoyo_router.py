from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from recursos_terapeuticos.app.schemas.recursos_terapeuticos.material_apoyo_schema import MaterialApoyoCreate, MaterialApoyoUpdate, MaterialApoyoOut
from recursos_terapeuticos.app.services.material_apoyo_service import get_material_apoyo, get_material_apoyo_by_id, create_material_apoyo, update_material_apoyo, delete_material_apoyo
from recursos_terapeuticos.app.shared.db.dependencies import get_db
from recursos_terapeuticos.app.shared.core.response_handler import success_response, error_response
from recursos_terapeuticos.app.shared.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from uuid import UUID
from typing import List

router = APIRouter(prefix="/materiales-apoyo")


@router.post("", response_model=MaterialApoyoOut)
def crear_material_apoyo(material_apoyo: MaterialApoyoCreate, db: Session = Depends(get_db)):
    try:
        material_apoyo_out = create_material_apoyo(db, material_apoyo)
        return success_response(HTTP_201_CREATED, "Material de apoyo creado con éxito", material_apoyo_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al crear material de apoyo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al crear material de apoyo", str(e))

@router.get("", response_model=List[MaterialApoyoOut])
def listar_materiales_apoyo(id_centro_rehabilitacion: UUID, db: Session = Depends(get_db)):
    try:
        materiales_apoyo = get_material_apoyo(db, id_centro_rehabilitacion)
        return success_response(HTTP_200_OK, "Materiales de apoyo listados con éxito", [material_apoyo.model_dump(mode="json") for material_apoyo in materiales_apoyo])
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al listar materiales de apoyo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar materiales de apoyo", str(e))

@router.get("/{id_material_apoyo}", response_model=MaterialApoyoOut)
def obtener_material_apoyo(id_material_apoyo: UUID, db: Session = Depends(get_db)):
    try:
        material_apoyo = get_material_apoyo_by_id(db, id_material_apoyo)
        return success_response(HTTP_200_OK, "Material de apoyo obtenido con éxito", material_apoyo.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al obtener material de apoyo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al obtener material de apoyo", str(e))

@router.put("/{id_material_apoyo}", response_model=MaterialApoyoOut)
def actualizar_material_apoyo(id_material_apoyo: UUID, material_apoyo: MaterialApoyoUpdate, db: Session = Depends(get_db)):
    try:
        material_apoyo_out = update_material_apoyo(db, id_material_apoyo, material_apoyo)
        return success_response(HTTP_200_OK, "Material de apoyo actualizado con éxito", material_apoyo_out.model_dump(mode="json"))
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al actualizar material de apoyo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar material de apoyo", str(e))

@router.delete("/{id_material_apoyo}")
def eliminar_material_apoyo(id_material_apoyo: UUID, db: Session = Depends(get_db)):
    try:
        delete_material_apoyo(db, id_material_apoyo)
        return success_response(HTTP_200_OK, "Material de apoyo eliminado con éxito")
    except ValueError as e:
        return error_response(HTTP_400_BAD_REQUEST, "Error al eliminar material de apoyo", str(e))
    except HTTPException as e:
        return error_response(e.status_code, e.detail)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar material de apoyo", str(e))