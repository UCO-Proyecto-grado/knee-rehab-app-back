from fastapi import APIRouter
from lambda_lesiones.api.v1.endpoints.categoria_router import router as categoria_router
from lambda_lesiones.api.v1.endpoints.tipo_lesion_router import router as tipo_lesion_router



router = APIRouter(tags=["Lesiones"])

router.include_router(categoria_router, prefix="/categorias", tags=["Categorias"])
router.include_router(tipo_lesion_router, prefix="/tipos-lesion", tags=["Tipos de Lesión"])