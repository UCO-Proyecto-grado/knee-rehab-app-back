from fastapi import APIRouter
from app.api.v1.endpoints import rehab

router = APIRouter()
router.include_router(rehab.router, prefix="/rehab", tags=["Rehabilitation"])
