from fastapi import FastAPI # type: ignore
from lambda_entidades_primarias.api.v1.router import router as api_router
from mangum import Mangum
from shared.core.cors import add_cors

app = FastAPI(title="KneeRehab API - Entidades Primarias")
add_cors(app)
app.include_router(api_router, prefix="/entidades-primarias")
handler = Mangum(app)
