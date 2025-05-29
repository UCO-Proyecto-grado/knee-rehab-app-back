from fastapi import FastAPI
from mangum import Mangum
from autentificador.app.shared.core.cors import add_cors
from autentificador.app.endpoints import login_router, paciente_router

app = FastAPI(docs_url="/docsAutentificador",openapi_url="/docsautentificador.json",redoc_url=None)

app.title = "utentificacion"
app.version = "0.0.1"
app.description = "Api for knee rehab Autentificador"

add_cors(app)

app.include_router(login_router.router)
app.include_router(paciente_router.router)
handler = Mangum(app)