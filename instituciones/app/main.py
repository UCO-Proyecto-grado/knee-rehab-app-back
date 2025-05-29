from fastapi import FastAPI
from instituciones.app.endpoints import centro_rehabilitacion_router, fisioterapeuta_sede_router, sede_router, tipo_sede_router
from mangum import Mangum
from instituciones.app.shared.core.cors import add_cors


app = FastAPI(docs_url="/docs",openapi_url="/docsInstituciones.json",redoc_url=None)

app.title = "Instituciones"
app.version = "0.0.1"
app.description = "Api for knee rehab instituciones"

add_cors(app)
app.include_router(centro_rehabilitacion_router.router)
app.include_router(fisioterapeuta_sede_router.router)
app.include_router(sede_router.router)
app.include_router(tipo_sede_router.router)

handler = Mangum(app)