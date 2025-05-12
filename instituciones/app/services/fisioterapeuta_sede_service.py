from sqlalchemy.orm import Session
from uuid import UUID
from instituciones.app.models.fisioterapeuta_sede_model import FisioterapeutaSede
from instituciones.app.schemas.fisioterapeuta_sede_schema import FisioterapeutaSedeCreate

def create_fisioterapeuta_sede(db: Session, data: FisioterapeutaSedeCreate):
    existe = db.query(FisioterapeutaSede).filter_by(
        id_fisioterapeuta=data.id_fisioterapeuta,
        id_sede=data.id_sede
    ).first()
    if existe:
        return None
    
    nueva_relacion = FisioterapeutaSede(**data.model_dump())
    db.add(nueva_relacion)
    db.commit()
    db.refresh(nueva_relacion)
    return nueva_relacion

def get_fisioterapeuta_sede_by_fisioterapeuta_id(db: Session, id_fisioterapeuta: UUID):
    return db.query(FisioterapeutaSede).filter_by(id_fisioterapeuta=id_fisioterapeuta).all()

def get_fisioterapeuta_sede_by_sede_id(db: Session, id_sede: UUID):
    return db.query(FisioterapeutaSede).filter_by(id_sede=id_sede).all()

def delete_fisioterapeuta_sede(db: Session, id_fisioterapeuta_sede: UUID):
    relacion = db.query(FisioterapeutaSede).filter_by(id=id_fisioterapeuta_sede).first()
    if relacion:
        db.delete(relacion)
        db.commit()
    return relacion

def get_fisioterapeuta_sede(db: Session, id_fisioterapeuta: UUID):
    relaciones = db.query(FisioterapeutaSede).filter_by(id_fisioterapeuta=id_fisioterapeuta).all()
    return relaciones
