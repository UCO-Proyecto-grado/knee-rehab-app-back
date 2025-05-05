from fastapi import APIRouter
from lambda_entidades_primarias.api.v1.endpoints.pais_router import router as pais_router
from lambda_entidades_primarias.api.v1.endpoints.departamento_router import router as departamento_router
from lambda_entidades_primarias.api.v1.endpoints.ciudad_router import router as ciudad_router
from lambda_entidades_primarias.api.v1.endpoints.tipo_identificacion_router import router as tipo_dni_router
from lambda_entidades_primarias.api.v1.endpoints.estado_router import router as estado_router



router = APIRouter(tags=["Entidades Primarias"])
router.include_router(pais_router, prefix="/paises", tags=["Paises"])
router.include_router(departamento_router, prefix="/departamentos", tags=["Departamentos"])
router.include_router(ciudad_router, prefix="/ciudades", tags=["Ciudades"])
router.include_router(tipo_dni_router, prefix="/tipos-dni", tags=["Tipos_dni"])
router.include_router(estado_router, prefix="/estados", tags=["Estados"])
