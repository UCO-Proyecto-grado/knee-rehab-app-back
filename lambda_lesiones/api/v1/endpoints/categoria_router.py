from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from lambda_lesiones.schemas.categoria_schema import CategoriaCreate, CategoriaOut
from lambda_lesiones.services import categoria_service
from shared.db.dependencies import get_db
from shared.core.response_handler import success_response, error_response
from shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter(tags=["Categorias"])

@router.post("", response_model=CategoriaOut)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    try:
        nueva = categoria_service.create_categoria(db, categoria.nombre)
        data = CategoriaOut.model_validate(nueva).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Categoría creada correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear la categoría", str(e))

@router.get("", response_model=List[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    try:
        items = categoria_service.get_categorias(db)
        data = [CategoriaOut.model_validate(c).model_dump(mode="json") for c in items]
        return success_response(HTTP_200_OK, "Categorías listadas", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar categorías", str(e))

@router.get("/{categoria_id}", response_model=CategoriaOut)
def obtener_categoria(categoria_id: UUID, db: Session = Depends(get_db)):
    try:
        c = categoria_service.get_categoria_by_id(db, categoria_id)
        if not c:
            return error_response(HTTP_404_NOT_FOUND, "Categoría no encontrada", "ID inválido o no existe")
        data = CategoriaOut.model_validate(c).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar categoría", str(e))

@router.put("/{categoria_id}", response_model=CategoriaOut)
def actualizar_categoria(categoria_id: UUID, categoria: CategoriaCreate, db: Session = Depends(get_db)):
    try:
        actualizada = categoria_service.update_categoria(db, categoria_id, categoria.nombre)
        data = CategoriaOut.model_validate(actualizada).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Categoría actualizada correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar categoría", str(e))

@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: UUID, db: Session = Depends(get_db)):
    try:
        categoria_service.delete_categoria(db, categoria_id)
        return success_response(HTTP_200_OK, "Categoría eliminada", {"id": str(categoria_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar categoría", str(e))
