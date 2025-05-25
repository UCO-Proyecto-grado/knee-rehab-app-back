from autentificador.app.shared.auth.cognito_client import create_cognito_user
from autentificador.app.schemas.paciente_schema import PacienteCreate
from uuid import uuid4

async def crear_paciente(data: PacienteCreate):
    # Crear en Cognito
    user_id = await create_cognito_user(data)

    # Aquí luego haces insert en tu tabla paciente si conectas DB

    return {
        "status": 201,
        "message": "Paciente creado exitosamente",
        "data": {
            "id": str(user_id),
            "email": data.email
        }
    }
