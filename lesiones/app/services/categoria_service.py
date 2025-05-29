from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lesiones.app.models.categoria_model import Categoria
from lesiones.app.shared.utils.logging_config import get_logger
from lesiones.app.shared.utils.log_messages import LogMessages
import uuid

logger = get_logger(__name__)


def create_categoria(db: Session, nombre: str):
    logger.info(f"{LogMessages.Categoria.CREATE_ATTEMPT} - Nombre: {nombre}")
    try:
        existente = db.query(Categoria).filter(Categoria.nombre.ilike(nombre)).first()
        if existente:
            logger.warning(f"{LogMessages.Categoria.DUPLICATE} - Nombre: {nombre}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría ya existe")

        nueva = Categoria(nombre=nombre)
        db.add(nueva)
        db.commit()
        db.refresh(nueva)

        logger.info(f"{LogMessages.Categoria.CREATE_SUCCESS} - ID: {nueva.id}")
        return nueva
    except Exception as e:
        logger.error(f"{LogMessages.Categoria.CREATE_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al crear categoría")


def get_categorias(db: Session):
    logger.info(LogMessages.Categoria.FETCH_ALL)
    try:
        return db.query(Categoria).all()
    except Exception as e:
        logger.error(f"{LogMessages.Categoria.FETCH_ALL_FAIL} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al listar categorías")


def get_categoria_by_id(db: Session, categoria_id: uuid.UUID):
    logger.info(f"{LogMessages.Categoria.FETCH_BY_ID} - ID: {categoria_id}")
    try:
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
        if not categoria:
            logger.warning(f"{LogMessages.Categoria.NOT_FOUND} - ID: {categoria_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
        return categoria
    except Exception as e:
        logger.error(f"{LogMessages.Categoria.FETCH_BY_ID_FAIL} - ID: {categoria_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al buscar categoría")


def update_categoria(db: Session, categoria_id: uuid.UUID, nombre: str):
    logger.info(f"{LogMessages.Categoria.UPDATE_ATTEMPT} - ID: {categoria_id}")
    try:
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
        if not categoria:
            logger.warning(f"{LogMessages.Categoria.NOT_FOUND} - ID: {categoria_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")

        categoria.nombre = nombre
        db.commit()
        db.refresh(categoria)

        logger.info(f"{LogMessages.Categoria.UPDATE_SUCCESS} - ID: {categoria_id}")
        return categoria
    except Exception as e:
        logger.error(f"{LogMessages.Categoria.UPDATE_FAIL} - ID: {categoria_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al actualizar categoría")


def delete_categoria(db: Session, categoria_id: uuid.UUID):
    logger.info(f"{LogMessages.Categoria.DELETE_ATTEMPT} - ID: {categoria_id}")
    try:
        categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
        if not categoria:
            logger.warning(f"{LogMessages.Categoria.NOT_FOUND} - ID: {categoria_id}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")

        db.delete(categoria)
        db.commit()

        logger.info(f"{LogMessages.Categoria.DELETE_SUCCESS} - ID: {categoria_id}")
        return categoria
    except Exception as e:
        logger.error(f"{LogMessages.Categoria.DELETE_FAIL} - ID: {categoria_id} - Error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno al eliminar categoría")
