from fastapi import FastAPI
from lambda_acceso_personal.api.v1.router import router as api_router
from mangum import Mangum
 
app = FastAPI(title="KneeRehab API - Lesiones")
app.include_router(api_router, prefix="/lesiones")
handler = Mangum(app)
 