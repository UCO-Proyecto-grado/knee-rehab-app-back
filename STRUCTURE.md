# Estructura del Proyecto Knee Rehabilitation App Backend

## Estructura de Directorios

```
knee-rehab-app-back/
├── .venv/                      # Entorno virtual de Python
├── lambda_lesiones/ # Funciones Lambda para entidades primarias
├── shared/                     # Código compartido entre lambdas
├── .git/                       # Directorio de control de versiones
├── tests/                      # Pruebas del proyecto
├── README.md                   # Documentación principal del proyecto
├── requirements.txt            # Dependencias del proyecto
├── handler.py                  # Manejador principal de la aplicación
├── serverless.yml             # Configuración de Serverless Framework
└── .gitignore                 # Archivos ignorados por git
```

## Descripción de Componentes

### Directorios Principales

- **.venv/**: Contiene el entorno virtual de Python con todas las dependencias del proyecto.
- **lambda_lesiones/**: Contiene las funciones Lambda que manejan las entidades primarias de la aplicación.
- **shared/**: Código compartido entre diferentes funciones Lambda para evitar duplicación.
- **tests/**: Contiene las pruebas unitarias y de integración del proyecto.

### Archivos de Configuración

- **requirements.txt**: Lista todas las dependencias de Python necesarias para el proyecto.
- **serverless.yml**: Archivo de configuración para Serverless Framework que define los servicios y funciones Lambda.
- **.gitignore**: Especifica los archivos y directorios que Git debe ignorar.

### Archivos de Código

- **handler.py**: Punto de entrada principal de la aplicación que maneja las solicitudes entrantes.

## Dependencias del Proyecto

El proyecto utiliza las siguientes dependencias principales:

### Framework y Servidor
- **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python.
- **Uvicorn**: Servidor ASGI de alto rendimiento para ejecutar aplicaciones FastAPI.
- **Mangum**: Adaptador para ejecutar aplicaciones ASGI en AWS Lambda.

### Base de Datos
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interactuar con la base de datos.
- **psycopg2-binary**: Adaptador PostgreSQL para Python, necesario para la conexión con la base de datos.

### Utilidades
- **python-dotenv**: Para cargar variables de entorno desde archivos .env.
- **pydantic**: Biblioteca para validación de datos y configuración de aplicaciones usando anotaciones de tipo Python.

## Notas Adicionales

- El proyecto utiliza Serverless Framework para el despliegue de funciones Lambda.
- La estructura está diseñada para seguir las mejores prácticas de desarrollo serverless.
- El código compartido en el directorio `shared/` ayuda a mantener la consistencia y reduce la duplicación de código. 