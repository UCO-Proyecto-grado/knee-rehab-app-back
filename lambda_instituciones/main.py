from fastapi import FastAPI
from lambda_instituciones.api.v1.router import router as api_router
from mangum import Mangum

app = FastAPI(title="KneeRehab API - Instituciones")
app.include_router(api_router, prefix="/api")
handler = Mangum(app)