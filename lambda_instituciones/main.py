from fastapi import FastAPI
from lambda_instituciones.api.v1.router import router as api_router
from mangum import Mangum
from shared.core.cors import add_cors

app = FastAPI(title="KneeRehab API - Instituciones")
add_cors(app)
app.include_router(api_router, prefix="/instituciones")
handler = Mangum(app)