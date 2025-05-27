from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_name: str
    database_user: str
    database_password: str

    ACCESS_KEY_AWS: str
    SECRET_KEY_AWS: str
    COGNITO_CLIENT_ID: str
    COGNITO_CLIENT_SECRET: str
    COGNITO_METADATA_URL: str
    USER_POOL_ID: str

    class Config:
        env_file = ".env"

settings = Settings()
