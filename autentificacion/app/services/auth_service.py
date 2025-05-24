import asyncio
from autentificacion.app.shared.auth.http_client import post_token_exchange
from autentificacion.app.shared.auth.auth import decode_id_token
from autentificacion.app.models.user import UsuarioAdministrador
from datetime import datetime
import base64

COGNITO_DOMAIN = "https://us-east-1zu66egizv.auth.us-east-1.amazoncognito.com"
CLIENT_ID = "18ojcokska1igo3hrb743d6bt5"
REDIRECT_URI = "https://develop.d3d4ljvzw46psr.amplifyapp.com/dashboard/"
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
    print(data)
    print(headers)
    return await post_token_exchange(url, data, headers)

def build_usuario_administrador(claims: dict) -> UsuarioAdministrador:
    now = datetime.utcnow().isoformat() + "Z"
    grupos = claims.get("cognito:groups", [])
    return UsuarioAdministrador(
        id=claims.get("sub"),
        user_name=claims.get("cognito:username"),
        primer_nombre=claims.get("given_name", ""),
        segundo_nombre=claims.get("middle_name"),
        primer_apellido=claims.get("family_name", ""),
        segundo_apellido=None,
        cedula="12345678",  # Aquí puedes consultar BD si quieres
        email=claims.get("email", ""),
        foto=None,
        created_at=now,
        updated_at=now,
        roles=grupos
    )

async def login_flow(code: str):
    tokens = await exchange_code_for_tokens(code)
    id_token = tokens.get("id_token")
    access_token = tokens.get("access_token")

    claims = decode_id_token(id_token)
    usuario = build_usuario_administrador(claims)

    return {
        "status": 201,
        "message": "Login exitoso",
        "data": {
            "usuario_administrador": usuario,
            "token": f"Bearer {access_token}"
        }
    }
