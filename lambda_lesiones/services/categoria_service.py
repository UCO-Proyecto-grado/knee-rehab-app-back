from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_lesiones.models.categoria_model import Categoria
import uuid

def create_categoria(db: Session, nombre: str):
    existente = db.query(Categoria).filter(Categoria.nombre.ilike(nombre)).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría ya existe")

    nueva = Categoria(nombre=nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def get_categorias(db: Session):
    return db.query(Categoria).all()

def get_categoria_by_id(db: Session, categoria_id: uuid.UUID):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def update_categoria(db: Session, categoria_id: uuid.UUID, nombre: str):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")

    categoria.nombre = nombre
    db.commit()
    db.refresh(categoria)
    return categoria

def delete_categoria(db: Session, categoria_id: uuid.UUID):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")

    db.delete(categoria)
    db.commit()
    return categoria
