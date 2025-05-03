# KneeRehab App – Arquitectura Serverless

Este proyecto implementa un sistema modular y escalable para la gestión de procesos de rehabilitación de rodilla usando **AWS Lambda** y **FastAPI**, con una estructura basada en **carpetas compartidas (shared)** reutilizables entre múltiples funciones Lambda.

---

## 📁 Estructura del Proyecto

```
knee-rehab-app/
│
├── shared/                  # Código común reutilizable (db, core, utils)
├── lambda_rehab/            # Lambda principal para gestionar la rehabilitación
├── tests/                   # Pruebas unitarias
├── .env                     # Variables de entorno
├── serverless.yml           # Configuración de Serverless Framework
├── requirements.txt         # Dependencias del proyecto
└── .venv/                   # Entorno virtual local (NO se sube a producción)
```

---

## 🚀 Requisitos Previos

- Python 3.10+
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started)
- Cuenta en AWS con credenciales configuradas localmente
- PostgreSQL en local o en RDS para desarrollo

---

## ✅ Instalación y Configuración Local

### 1. Clonar el proyecto y crear entorno virtual

```bash
git clone https://tu-repo/knee-rehab-app.git
cd knee-rehab-app
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---
### 3. Configurar variables de entorno

Crear el archivo `.env` en la raiz del proyecto siguiente la siguiente estructura:

```bash
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
```

---

## 🧪 Ejecución Local (Desarrollo)

### Ejecutar todas las lambdas(`local_main.py`) con Uvicorn

```bash
uvicorn local_main:app --reload
```
### Ejecutar Lambda especifica (`lambda_instituciones`) con Uvicorn

```bash
uvicorn lambda_rehab.main:app --reload
```

### Ejecutar pruebas

```bash
pytest tests/
```

---

## ⚙️ Despliegue en AWS con Serverless Framework

### 1. Configurar credenciales AWS en tu máquina

```bash
aws configure
```

### 2. Desplegar

```bash
sls deploy
```

Esto empaquetará tu Lambda desde `lambda_rehab/` e incluirá automáticamente `shared/` como capa o parte del paquete.

---

## 📦 Estructura recomendada por función

Puedes crear múltiples Lambdas con esta estructura:

```
lambda_rehab/
lambda_auth/
lambda_notify/
```

Todas reutilizando módulos de:

```
shared/db/
shared/core/
shared/utils/
```

---

## 🔐 Buenas prácticas

- No subir `.venv` ni `.env` a repositorios remotos.
- Evitar código duplicado entre Lambdas. Usa `shared/`.
- Versiona tus endpoints y mantén documentada tu API.

---

## Documentacion de API 

Una vez la aplicacion este corriendo, se tendra acceso a la documentacion mediante los siguientes parametros:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 📬 Contacto

Proyecto desarrollado por Sebastian Ramirez y Harby Garcia Grajales – **KneeRehab App**
Repositorio educativo – Proyecto de grado UCO - Ingenieria de sistemas – 2025
