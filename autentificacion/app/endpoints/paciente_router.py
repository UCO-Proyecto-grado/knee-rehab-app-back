from fastapi import APIRouter, Depends, HTTPException
from autentificacion.app.schemas.paciente_schema import PacienteCreate
from autentificacion.app.services import paciente_service
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth")

@router.post("/paciente")
async def crear_paciente(data: PacienteCreate):
    try:
        result = await paciente_service.crear_paciente(data)
        return JSONResponse(status_code=201, content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
