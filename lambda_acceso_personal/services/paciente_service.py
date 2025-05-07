from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from lambda_acceso_personal.models.paciente_model import Paciente
import uuid

def create_paciente(db: Session, data: dict):
    existente = db.query(Paciente).filter(Paciente.identificacion == data["identificacion"]).first()
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Paciente ya registrado")

    paciente = Paciente(**data)
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente

def get_pacientes(db: Session):
    return db.query(Paciente).all()

def get_paciente_by_id(db: Session, paciente_id: uuid.UUID):
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()

def update_paciente(db: Session, paciente_id: uuid.UUID, data: dict):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")
    
    for key, value in data.items():
        setattr(paciente, key, value)
    
    db.commit()
    db.refresh(paciente)
    return paciente

def delete_paciente(db: Session, paciente_id: uuid.UUID):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")

    db.delete(paciente)
    db.commit()
    return paciente
