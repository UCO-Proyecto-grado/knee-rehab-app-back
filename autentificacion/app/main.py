from fastapi import FastAPI
from mangum import Mangum
from autentificacion.app.shared.core.cors import add_cors
from autentificacion.app.endpoints import login_router, paciente_router

app = FastAPI(docs_url="/docsAutentificacion",openapi_url="/docsAutentificacion.json",redoc_url=None)

app.title = "utentificacion"
app.version = "0.0.1"
app.description = "Api for knee rehab Autentificacion"

add_cors(app)

app.include_router(login_router.router)
app.include_router(paciente_router.router)
handler = Mangum(app)