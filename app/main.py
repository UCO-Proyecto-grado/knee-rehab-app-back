from fastapi import FastAPI
from app.api.v1.router import router as api_router

app = FastAPI(title="KneeRehab API")

# Rutas
app.include_router(api_router, prefix="/api/v1")
