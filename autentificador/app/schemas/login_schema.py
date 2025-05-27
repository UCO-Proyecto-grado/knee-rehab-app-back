from pydantic import BaseModel, EmailStr
from datetime import date
from uuid import UUID

class LoginRequest(BaseModel):
    code: str

class TipoIdentificacionBasicOut(BaseModel):
    nombre: str
    codigo: str

    class Config:
        from_attributes = True

class EstadoBasicOut(BaseModel):
    nombre: str

    class Config:
        from_attributes = True

class PaisBasicOut(BaseModel):
    nombre: str

    class Config:
        from_attributes = True

class DepartamentoBasicOut(BaseModel):
    nombre: str
    pais: PaisBasicOut

    class Config:
        from_attributes = True

class CiudadBasicOut(BaseModel):
    nombre: str
    departamento: DepartamentoBasicOut 
    
    class Config:
        from_attributes = True  

class PacienteOut(BaseModel):
    id: UUID
    id_cognito: str
    identificacion: str
    nombre: str
    apellido: str
    genero: str
    fecha_nacimiento: date
    telefono: str | None = None
    telefono_validado: bool = False
    email: EmailStr
    email_validado: bool = False
    contrasena: str
    direccion: str | None = None
    tipo_identificacion: TipoIdentificacionBasicOut
    estado: EstadoBasicOut
    ciudad: CiudadBasicOut
    
    class Config:
        from_attributes = True

class UsuarioAdministradorOut(BaseModel):
    id: str
    email: str
    usuario: PacienteOut
    roles: list[str]

class LoginResponse(BaseModel):
    status: int
    message: str
    data: dict
