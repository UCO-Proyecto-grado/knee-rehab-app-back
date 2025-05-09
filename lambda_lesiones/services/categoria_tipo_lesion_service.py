from sqlalchemy.orm import Session
from uuid import UUID
from lambda_lesiones.models.categoria_tipo_lesion_model import CategoriaTipoLesion
from lambda_lesiones.schemas.categoria_tipo_lesion_schema import CategoriaTipoLesionCreate


def create_relacion(db: Session, data: CategoriaTipoLesionCreate):
    existe = db.query(CategoriaTipoLesion).filter_by(
        id_categoria=data.id_categoria,
        id_lesion=data.id_lesion
    ).first()
    if existe:
        return None  # Ya existe

    nueva_relacion = CategoriaTipoLesion(**data.model_dump())
    db.add(nueva_relacion)
    db.commit()
    db.refresh(nueva_relacion)
    return nueva_relacion


def get_relaciones(db: Session):
    return db.query(CategoriaTipoLesion).all()


def delete_relacion(db: Session, id_relacion: UUID):
    relacion = db.query(CategoriaTipoLesion).filter_by(id=id_relacion).first()
    if relacion:
        db.delete(relacion)
        db.commit()
    return relacion
