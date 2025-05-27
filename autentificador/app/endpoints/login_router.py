from fastapi import APIRouter, Depends, HTTPException, status
from autentificador.app.schemas.login_schema import LoginRequest, LoginResponse
from autentificador.app.services import auth_service
from autentificador.app.schemas.login_schema import UsuarioAdministradorOut
from fastapi.responses import JSONResponse
import asyncio

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest):
    try:
        result = await auth_service.login_flow(data.code)
        usuario_dict = result["data"]["usuario_administrador"].__dict__
        result["data"]["usuario_administrador"] = usuario_dict
        return JSONResponse(status_code=201, content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
