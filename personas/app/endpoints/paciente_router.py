from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from personas.app.schemas.acceso_personal.paciente_schema import PacienteCreate, PacienteOut
from personas.app.services import paciente_service
from personas.app.shared.db.dependencies import get_db
from personas.app.shared.core.response_handler import success_response, error_response
from personas.app.shared.utils.constants import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

router = APIRouter(prefix="/paciente")

@router.post("", response_model=PacienteOut)
def crear_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    try:
        nuevo = paciente_service.create_paciente(db, paciente.model_dump())
        data = PacienteOut.model_validate(nuevo).model_dump(mode="json")
        return success_response(HTTP_201_CREATED, "Paciente creado correctamente", data)
    except Exception as e:
        return error_response(HTTP_400_BAD_REQUEST, "No se pudo crear el paciente", str(e))

@router.get("", response_model=List[PacienteOut])
def listar_pacientes(db: Session = Depends(get_db)):
    try:
        pacientes = paciente_service.get_pacientes(db)
        data = [PacienteOut.model_validate(p).model_dump(mode="json") for p in pacientes]
        return success_response(HTTP_200_OK, "Pacientes listados", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar pacientes", str(e))

@router.get("/{paciente_id}", response_model=PacienteOut)
def obtener_paciente(paciente_id: UUID, db: Session = Depends(get_db)):
    try:
        p = paciente_service.get_paciente_by_id(db, paciente_id)
        if not p:
            return error_response(HTTP_404_NOT_FOUND, "Paciente no encontrado", "ID inválido o no existe")
        data = PacienteOut.model_validate(p).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Consulta exitosa", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al consultar paciente", str(e))
    
@router.get("/sede/{sede_id}", response_model=List[PacienteOut])
def obtener_pacientes_por_sede(sede_id: UUID, db: Session = Depends(get_db)):
    try:
        pacientes_orm = paciente_service.get_pacientes_by_sede_id(db, sede_id)
        # Validate each Paciente ORM object into PacienteOut schema
        data = [PacienteOut.model_validate(p).model_dump(mode='json') for p in pacientes_orm]
        return success_response(HTTP_200_OK, "Pacientes Listados con éxito", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al listar pacientes", str(e))
    


# @router.get("", response_model=List[ModuloOut])
# def listar_modulos(id_centro: UUID, db: Session = Depends(get_db)):
#     try:
#         modulos = get_modulos(db, id_centro)
#         return success_response(HTTP_200_OK, "Modulos listados con éxito", [modulo.model_dump(mode="json") for modulo in modulos])
#     except ValueError as e:
#         return error_response(HTTP_400_BAD_REQUEST, "Error al listar modulos", str(e))
#     except HTTPException as e:
#         return error_response(e.status_code, e.detail)
#     except Exception as e:    

@router.put("/{paciente_id}", response_model=PacienteOut)
def actualizar_paciente(paciente_id: UUID, paciente: PacienteCreate, db: Session = Depends(get_db)):
    try:
        actualizado = paciente_service.update_paciente(db, paciente_id, paciente.model_dump())
        data = PacienteOut.model_validate(actualizado).model_dump(mode="json")
        return success_response(HTTP_200_OK, "Paciente actualizado correctamente", data)
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al actualizar paciente", str(e))

@router.delete("/{paciente_id}")
def eliminar_paciente(paciente_id: UUID, db: Session = Depends(get_db)):
    try:
        paciente_service.delete_paciente(db, paciente_id)
        return success_response(HTTP_200_OK, "Paciente eliminado", {"id": str(paciente_id)})
    except Exception as e:
        return error_response(HTTP_500_INTERNAL_SERVER_ERROR, "Error al eliminar paciente", str(e))