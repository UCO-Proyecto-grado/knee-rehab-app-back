from fastapi import FastAPI

# Importa solo los routers raíz de cada lambda
from lambda_entidades_primarias.api.v1.router import router as entidades_router
from lambda_instituciones.api.v1.router import router as instituciones_router

app = FastAPI(
    title="KneeRehab - API local unificada",
    description="Servidor local para desarrollar y probar múltiples Lambdas de forma integrada.",
    version="1.0.0"
)

# Incluir cada router raíz UNA SOLA VEZ con prefijos distintos
app.include_router(entidades_router, prefix="/api/v1", tags=["Entidades Primarias"])
app.include_router(instituciones_router, prefix="/api/v1", tags=["Instituciones"])
# Puedes agregar: /rehab, /pacientes, etc.