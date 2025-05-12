from fastapi import APIRouter
from entidades_primarias.app.endpoints.pais_router import router as pais_router
from entidades_primarias.app.endpoints.departamento_router import router as departamento_router
from entidades_primarias.app.endpoints.ciudad_router import router as ciudad_router
from entidades_primarias.app.endpoints.tipo_identificacion_router import router as tipo_dni_router
from entidades_primarias.app.endpoints.estado_router import router as estado_router



router = APIRouter(tags=["Entidades Primarias"])
router.include_router(pais_router, prefix="/paises")
router.include_router(departamento_router, prefix="/departamentos")
router.include_router(ciudad_router, prefix="/ciudades")
router.include_router(tipo_dni_router, prefix="/tipos-dni")
router.include_router(estado_router, prefix="/estados")
