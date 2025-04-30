from sqlalchemy import text
from shared.db.session import SessionLocal

def test_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("✅ Conexión exitosa a la base de datos.")
    except Exception as e:
        print("❌ Error al conectar con la base de datos:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
