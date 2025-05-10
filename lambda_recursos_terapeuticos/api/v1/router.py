from fastapi import APIRouter
from lambda_recursos_terapeuticos.api.v1.endpoints.modulo_router import router as modulo_router
from lambda_recursos_terapeuticos.api.v1.endpoints.material_apoyo_router import router as material_apoyo_router
from lambda_recursos_terapeuticos.api.v1.endpoints.ejercicio_router import router as ejercicio_router
    
router = APIRouter(tags=["Recursos Terapéuticos"])
router.include_router(modulo_router, prefix="/modulos")
router.include_router(material_apoyo_router, prefix="/material-apoyo")
router.include_router(ejercicio_router, prefix="/ejercicios")

