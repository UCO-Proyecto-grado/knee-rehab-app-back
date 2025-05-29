from fastapi import FastAPI
from mangum import Mangum
from terapias.app.shared.core.cors import add_cors
from terapias.app.endpoints import estado_plan_rehabilitacion_ejercicio_router, paciente_categoria_tipo_lesion_router, plan_rehabilitacion_router

app = FastAPI(docs_url="/docsTerapias",openapi_url="/docsTerapias.json",redoc_url=None)

app.title = "Terapias"
app.version = "0.0.1"
app.description = "Api for knee rehab terapias"

add_cors(app)
# Incluir los routers de las rutas
app.include_router(estado_plan_rehabilitacion_ejercicio_router.router)
app.include_router(paciente_categoria_tipo_lesion_router.router)
app.include_router(plan_rehabilitacion_router.router)

handler = Mangum(app)