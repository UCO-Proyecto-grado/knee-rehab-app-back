from fastapi import FastAPI
from lambda_recursos_terapeuticos.api.v1.router import router as api_router
from mangum import Mangum
from shared.core.cors import add_cors

app = FastAPI(title="KneeRehab API - Recursos Terapéuticos")
add_cors(app)
app.include_router(api_router, prefix="/recursos-terapeuticos")
handler = Mangum(app)
 