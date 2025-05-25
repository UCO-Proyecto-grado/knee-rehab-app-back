from pydantic import BaseModel

class LoginRequest(BaseModel):
    code: str

class UsuarioAdministradorOut(BaseModel):
    id: str
    user_name: str
    primer_nombre: str
    segundo_nombre: str | None = None
    primer_apellido: str
    segundo_apellido: str | None = None
    cedula: str | None = None
    email: str
    roles: list[str]
    created_at: str
    updated_at: str

class LoginResponse(BaseModel):
    status: int
    message: str
    data: dict
