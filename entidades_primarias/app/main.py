from fastapi import FastAPI
from mangum import Mangum
from entidades_primarias.app.shared.core.cors import add_cors
from entidades_primarias.app.endpoints import ciudad_router, pais_router, departamento_router, estado_router, tipo_identificacion_router

app = FastAPI(docs_url="/docsEntidadesPrimarias",openapi_url="/docsEntidadesPrimarias.json",redoc_url=None)

app.title = "Entidades Primarias"
app.version = "0.0.1"
app.description = "Api for knee rehab entidades primarias"

add_cors(app)
# Incluir los routers de las rutas
app.include_router(pais_router.router)
app.include_router(departamento_router.router)
app.include_router(ciudad_router.router)
app.include_router(tipo_identificacion_router.router)
app.include_router(estado_router.router)

@app.get("/statuslambda")
def ping():
    return {"message": "Corriendo"}


@app.get("/test")
def test_route():
    return {"status": "OK"}

handler = Mangum(app)