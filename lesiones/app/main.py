from fastapi import FastAPI
from mangum import Mangum
from lesiones.app.shared.core.cors import add_cors
from lesiones.app.endpoints import categoria_router, categoria_tipo_lesion_router, tipo_lesion_router

app = FastAPI(docs_url="/docsLesiones",openapi_url="/docsLesiones.json",redoc_url=None)

app.title = "Lesiones"
app.version = "0.0.1"
app.description = "Api for knee rehab lesiones"

add_cors(app)

app.include_router(categoria_router.router)
app.include_router(categoria_tipo_lesion_router.router)
app.include_router(tipo_lesion_router.router)

@app.get("/statuslambda")
def statuslambda():
    return {"message": "Corriendo"}

@app.get("/test")
def test_route():
    return {"status": "OK"}

handler = Mangum(app)
  