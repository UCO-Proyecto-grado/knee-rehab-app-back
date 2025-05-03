from fastapi import APIRouter
from lambda_entidades_primarias.api.v1.endpoints import health
from lambda_entidades_primarias.api.v1.endpoints.pais_router import router as pais_router

router = APIRouter()
router.include_router(health.router, prefix="", tags=["Health"])
router.include_router(pais_router, prefix="/paises", tags=["Paises"])