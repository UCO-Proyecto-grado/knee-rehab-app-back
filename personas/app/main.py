from fastapi import FastAPI
from personas.app.endpoints import paciente_router
from mangum import Mangum
from personas.app.shared.core.cors import add_cors


app = FastAPI(docs_url="/docsPersonas",openapi_url="/docsPersonas.json",redoc_url=None)

app.title = "Personas"
app.version = "0.0.1"
app.description = "Api for knee rehab personas"

add_cors(app)
app.include_router(paciente_router.router)
# app.include_router(fisioterapeuta_router.router)
# app.include_router(usuario_router.router)
# app.include_router(usuario_centro_rehabilitacion_router.router)
# app.include_router(usuario_sede_router.router)

handler = Mangum(app)