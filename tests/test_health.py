from sqlalchemy import text
from shared.db.session import SessionLocal

def test_health_check():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("✅ /health: conexión a la base de datos exitosa.")
    except Exception as e:
        print("❌ /health: error de conexión:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_health_check()