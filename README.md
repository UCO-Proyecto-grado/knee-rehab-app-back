# Knee Rehab App Backend

Este es el backend del proyecto KneeRehab. Construido en Python con FastAPI y desplegable en AWS Lambda usando arquitectura serverless.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Configuración Inicial

1. Crear un entorno virtual de Python:
```bash
Linux: 
python3 -m venv .venv ó 

Para ejecutar el servidor de desarrollo:
Windows:
py -m venv .venv

```

2. Activar el entorno virtual:
```bash
Linux: 
source .venv/bin/activate

Windows:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate

```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar la Aplicación

Para ejecutar el servidor de desarrollo:
```bash
uvicorn app.main:app --port 5001 --reload
```

La API estará disponible en:
- URL base: http://127.0.0.1:5001
- Documentación Swagger UI: http://127.0.0.1:5001/docs
- Especificación OpenAPI: http://127.0.0.1:5001/openapi.json

## Estructura del Proyecto

```
knee-rehab-app-back/
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── services/
├── tests/
├── requirements.txt
└── README.md
```

## Dependencias Principales

- FastAPI: Framework web moderno para APIs
- Uvicorn: Servidor ASGI
- Mangum: Adaptador para AWS Lambda
- Pydantic: Validación de datos y configuración

## Desarrollo

El servidor de desarrollo incluye:
- Recarga automática al detectar cambios
- Documentación interactiva de la API
- Validación automática de tipos

## Despliegue

El proyecto está configurado para ser desplegado en AWS Lambda usando arquitectura serverless.

## Contribución

1. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
2. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
3. Push a la rama (`git push origin feature/AmazingFeature`)
4. Abrir un Pull Request

