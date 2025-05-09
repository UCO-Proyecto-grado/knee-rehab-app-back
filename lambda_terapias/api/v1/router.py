from fastapi import APIRouter
from lambda_terapias.api.v1.endpoints.plan_rehabilitacion_router  import router as plan_rehabilitacion_router
from lambda_terapias.api.v1.endpoints.paciente_categoria_tipo_lesion_router import router as pctl_router
from lambda_terapias.api.v1.endpoints.estado_plan_rehabilitacion_ejercicio_router import router as estado_plan_router

router = APIRouter(tags=["Terapias"])
router.include_router(plan_rehabilitacion_router, prefix="/plan_rehabilitacion")
router.include_router(pctl_router, prefix="/paciente-categoria-tipo-lesion")
router.include_router(estado_plan_router, prefix="/estado-plan-rehabilitacion")

