from fastapi import FastAPI
from recursos_terapeuticos.app.endpoints.modulo_router import router as modulo_router
from recursos_terapeuticos.app.endpoints.material_apoyo_router import router as material_apoyo_router
from recursos_terapeuticos.app.endpoints.ejercicio_router import router as ejercicio_router
from mangum import Mangum
from recursos_terapeuticos.app.shared.core.cors import add_cors

app = FastAPI(docs_url="/docsRecursosTerapeuticos",openapi_url="/docsRecursosTerapeuticos.json",redoc_url=None)

app.title = "Recursos Terapéuticos"
app.version = "0.0.1"
app.description = "Api for knee rehab recursos terapéuticos"

add_cors(app)
app.include_router(modulo_router)
app.include_router(material_apoyo_router)
app.include_router(ejercicio_router)

handler = Mangum(app)