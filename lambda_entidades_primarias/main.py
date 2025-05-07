from fastapi import FastAPI
from lambda_entidades_primarias.api.v1.router import router as api_router
from mangum import Mangum

app = FastAPI(title="KneeRehab API - Entidades Primarias")
app.include_router(api_router, prefix="/entidades-primarias")
handler = Mangum(app)
