from fastapi import APIRouter
from lambda_instituciones.api.v1.endpoints.tipo_sede_router import router as tipo_sede_router
from lambda_instituciones.api.v1.endpoints.centro_rehabilitacion_router import router as centro_rehabilitacion_router

router = APIRouter(tags=["Instituciones"])

router.include_router(centro_rehabilitacion_router, prefix="/centro-rehabilitacion")
router.include_router(tipo_sede_router, prefix="/tipo-sede")