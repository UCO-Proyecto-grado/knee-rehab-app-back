from fastapi import FastAPI
from api.v1 import router as api_router
from mangum import Mangum
from shared.core.cors import add_cors

app = FastAPI(title="KneeRehab API - Recursos Terapéuticos")
add_cors(app)
app.include_router(api_router, prefix="/recursos-terapeuticos")
handler = Mangum(app)
 