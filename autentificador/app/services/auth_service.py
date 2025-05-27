from sqlalchemy.orm import Session
from autentificador.app.shared.auth.http_client import post_token_exchange
from autentificador.app.shared.auth.auth import decode_id_token
from autentificador.app.models.user import UsuarioAdministrador
from autentificador.app.shared.db.base import Paciente
from autentificador.app.schemas.login_schema import PacienteOut
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from autentificador.app.shared.db.session import SessionLocal
import base64

COGNITO_DOMAIN = "https://us-east-1zu66egizv.auth.us-east-1.amazoncognito.com"
CLIENT_ID = "18ojcokska1igo3hrb743d6bt5"
REDIRECT_URI = "https://develop.d3d4ljvzw46psr.amplifyapp.com/"
CLIENT_SECRET = "1eim1p0a80bkrks410u4mlk5795lon8jkldrte1dr9mge75jfvbo"


async def exchange_code_for_tokens(code: str):
    url = f"{COGNITO_DOMAIN}/oauth2/token"
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {b64_auth_str}"}
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    return await post_token_exchange(url, data, headers)


def get_paciente_by_id_cognito(db: Session, cognito_id: str) -> PacienteOut:
    try: 
        paciente = db.query(Paciente).filter(Paciente.id_cognito == cognito_id).first()
        if not paciente:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente no encontrado")
        return PacienteOut.model_validate(paciente).model_dump(mode="json")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al buscar paciente")


def build_usuario_administrador(db: Session, claims: dict) -> UsuarioAdministrador:
    now = datetime.utcnow().isoformat() + "Z"
    grupos = claims.get("cognito:groups", [])
    id_cognito = claims.get("sub")    
    usuario_bd = get_paciente_by_id_cognito(db, id_cognito)
    return UsuarioAdministrador(
        id_cognito=id_cognito,
        email=claims.get("email", ""),
        roles=grupos,
        usuario=usuario_bd
    )

async def login_flow(db: Session, code: str):
    tokens = await exchange_code_for_tokens(code)
    id_token = tokens.get("id_token")
    access_token = tokens.get("access_token")

    claims = decode_id_token(id_token)
    usuario = build_usuario_administrador(db, claims)

    return {
        "status": 201,
        "message": "Login exitoso",
        "data": {
            "usuario_administrador": usuario,
            "token": f"Bearer {access_token}"
        }
    }
