from fastapi import FastAPI
from shared.core.cors import add_cors
# Importa solo los routers raíz de cada lambda
from lambda_entidades_primarias.api.v1.router import router as entidades_router
from lambda_instituciones.api.v1.router import router as instituciones_router
from lambda_acceso_personal.api.v1.router import router as acceso_personal_router
from lambda_lesiones.api.v1.router import router as lesiones_router
from lambda_recursos_terapeuticos.api.v1.router import router as recursos_terapeuticos_router
from lambda_terapias.api.v1.router import router as terapias_router

app = FastAPI(
    title="KneeRehab - API local unificada",
    description="Servidor local para desarrollar y probar múltiples Lambdas de forma integrada.",
    version="1.0.0"
)

add_cors(app)

# Incluir cada router raíz UNA SOLA VEZ con prefijos distintos
app.include_router(entidades_router, prefix="/entidades-primarias", tags=["Entidades Primarias"])
app.include_router(instituciones_router, prefix="/instituciones", tags=["Instituciones"])
app.include_router(acceso_personal_router, prefix="/acceso-personal", tags=["Accesos personales"])
app.include_router(lesiones_router, prefix="/lesiones", tags=["Lesiones"])
app.include_router(recursos_terapeuticos_router, prefix="/recursos-terapeuticos", tags=["Recursos Terapéuticos"])
app.include_router(terapias_router, prefix="/terapias", tags=["Terapias"])
# Puedes agregar: /rehab, /pacientes, etc.