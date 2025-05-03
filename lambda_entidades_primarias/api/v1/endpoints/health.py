from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from shared.db.dependencies import get_db

router = APIRouter()

@router.get("/health", tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Conexión a la base de datos exitosa"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
