from fastapi import APIRouter
from lambda_entidades_primarias.api.v1.endpoints.pais_router import router as pais_router

router = APIRouter(tags=["Entidades Primarias"])
router.include_router(pais_router, prefix="/paises")