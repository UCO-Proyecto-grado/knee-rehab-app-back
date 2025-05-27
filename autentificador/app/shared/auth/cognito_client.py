import boto3
import uuid
from autentificador.app.shared.core.config import settings


async def create_cognito_user(data):
    #Van las credenciales del IAM de AWS
    client = boto3.client('cognito-idp', region_name='us-east-1', aws_access_key_id= settings.ACCESS_KEY_AWS, aws_secret_access_key= settings.SECRET_KEY_AWS)

    user_id = str(uuid.uuid4())
    client.admin_create_user(
        UserPoolId=settings.USER_POOL_ID,
        Username=data.email,
        UserAttributes=[
            {"Name": "email", "Value": data.email},
            {"Name": "given_name", "Value": data.nombre},
            {"Name": "family_name", "Value": data.apellido},
            {"Name": "phone_number", "Value": data.telefono},
            {"Name": "birthdate", "Value": str(data.fecha_nacimiento)},
            {"Name": "gender", "Value": data.genero},
        ],
        TemporaryPassword=data.password,
        MessageAction='SUPPRESS'
    )

    # Establecer contraseña definitiva
    client.admin_set_user_password(
        UserPoolId=settings.USER_POOL_ID,
        Username=data.email,
        Password=data.password,
        Permanent=True
    )

    # Añadir al grupo Paciente
    client.admin_add_user_to_group(
        UserPoolId=settings.USER_POOL_ID,
        Username=data.email,
        GroupName="Paciente"
    )

    return user_id
