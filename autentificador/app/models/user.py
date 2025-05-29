from dataclasses import dataclass
from typing import List, Optional
from autentificador.app.schemas.login_schema import PacienteOut

@dataclass
class UsuarioAdministrador:
    id_cognito: str
    email: str
    usuario: Optional[PacienteOut]
    roles: List[str]
