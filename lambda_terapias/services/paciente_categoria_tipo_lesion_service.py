from sqlalchemy.orm import Session
from uuid import UUID
from lambda_terapias.models.paciente_categoria_tipo_lesion_model import PacienteCategoriaTipoLesion
from lambda_terapias.schemas.paciente_categoria_tipo_lesion_schema import PacienteCategoriaTipoLesionCreate


def create_relacion(db: Session, data: PacienteCategoriaTipoLesionCreate):
    existe = db.query(PacienteCategoriaTipoLesion).filter_by(
        id_paciente=data.id_paciente,
        id_categoria_tipo_lesion=data.id_categoria_tipo_lesion
    ).first()
    if existe:
        return None
    nueva = PacienteCategoriaTipoLesion(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def get_all(db: Session):
    return db.query(PacienteCategoriaTipoLesion).all()


def delete_relacion(db: Session, relacion_id: UUID):
    relacion = db.query(PacienteCategoriaTipoLesion).filter_by(id=relacion_id).first()
    if relacion:
        db.delete(relacion)
        db.commit()
    return relacion
