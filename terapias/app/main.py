from fastapi import FastAPI
from lambda_instituciones.api.v1.router import router as api_router
from mangum import Mangum
from terapias.app.shared.core.cors import add_cors

app = FastAPI(title="KneeRehab API - Terapias")
add_cors(app)
app.include_router(api_router, prefix="/terapias")
handler = Mangum(app)