from pydantic import BaseModel, EmailStr
from datetime import date

class PacienteCreate(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    telefono: str
    fecha_nacimiento: date
    genero: str
