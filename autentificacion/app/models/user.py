from dataclasses import dataclass
from typing import List

@dataclass
class UsuarioAdministrador:
    id: str
    user_name: str
    primer_nombre: str
    segundo_nombre: str | None
    primer_apellido: str
    segundo_apellido: str | None
    cedula: str | None
    email: str
    foto: str | None
    created_at: str
    updated_at: str
    roles: List[str]
