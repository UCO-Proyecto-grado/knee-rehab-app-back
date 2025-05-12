from fastapi import FastAPI
from entidades_primarias.app.endpoints.router import router as api_router
from mangum import Mangum
from entidades_primarias.app.shared.core.cors import add_cors

app = FastAPI(title="KneeRehab API - Entidades Primarias")
add_cors(app)
app.include_router(api_router, prefix="/entidades-primarias")
handler = Mangum(app)


@app.get("/ping")
def ping():
    return {"message": "pong"}
