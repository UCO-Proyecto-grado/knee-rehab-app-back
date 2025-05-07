from fastapi import APIRouter
from lambda_acceso_personal.api.v1.endpoints.paciente_router import router as paciente_router
from lambda_acceso_personal.api.v1.endpoints.fisioterapeuta_router import router as fisioterapeuta_router



router = APIRouter(tags=["Accesos personales"])
router.include_router(paciente_router, prefix="/pacientes", tags=["Pacientes"])
router.include_router(fisioterapeuta_router, prefix="/fisioterapeutas", tags=["Fisioterapeutas"])
