from fastapi import APIRouter
from lambda_instituciones.api.v1.endpoints.tipo_sede_router import router as tipo_sede_router

router = APIRouter(tags=["Instituciones"])
router.include_router(tipo_sede_router, prefix="/tipo-sede")