# Knee Rehab App - Backend

Este es el backend de la aplicación Knee Rehab, desarrollado con FastAPI y desplegado en AWS Lambda.

## Requisitos Previos

- Python 3.10 o superior
- Node.js y npm
- Serverless Framework
- Git

## Configuración del Entorno Local

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd knee-rehab-app-back
```

### 2. Configurar el Entorno Virtual de Python

```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar el entorno virtual
# En macOS/Linux:
source .venv/bin/activate
# En Windows:
# .venv\Scripts\activate

# Instalar dependencias de Python
pip install -r requirements.txt
```

### 3. Instalar Dependencias de Serverless

```bash
# Instalar plugins necesarios
npm install --save-dev serverless-python-requirements serverless-offline
```

### 4. Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```plaintext
DATABASE_HOST=<host-de-la-base-de-datos>
DATABASE_PORT=<puerto>
DATABASE_NAME=<nombre-de-la-base-de-datos>
DATABASE_USER=<usuario>
DATABASE_PASSWORD=<contraseña>
```

## Ejecutar la Lambda Localmente

### 1. Verificar Puertos

Asegúrate de que los puertos 3000 y 3002 estén disponibles. Si necesitas liberarlos:

```bash
# En macOS/Linux:
lsof -ti:3000 | xargs kill -9 || true
lsof -ti:3002 | xargs kill -9 || true

# En Windows:
# netstat -ano | findstr :3000
# netstat -ano | findstr :3002
# taskkill /PID <PID> /F
```

### 2. Iniciar el Servidor Local

```bash
# Asegúrate de que el entorno virtual esté activado
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Iniciar el servidor
sls offline
```

El servidor estará disponible en:
- API: http://localhost:3000
- Documentación: http://localhost:3000/docs

### 3. Detener el Servidor

Para detener el servidor, presiona `Ctrl+C` o `Command+C` en la terminal.

## Estructura del Proyecto

```
knee-rehab-app-back/
├── .env                    # Variables de entorno
├── .venv/                  # Entorno virtual de Python
├── instituciones/          # Código fuente
│   └── app/
│       ├── main.py        # Punto de entrada
│       └── ...
├── requirements.txt        # Dependencias de Python
├── serverless.yml         # Configuración de Serverless
└── README.md              # Este archivo
```

## Solución de Problemas Comunes

### El comando `sls offline` no se encuentra
- Verifica que los plugins estén instalados
- Reinstala los plugins con npm
```bash
npm install --save-dev serverless-python-requirements serverless-offline
```

### Errores de conexión a la base de datos
- Verifica que el archivo `.env` existe y tiene los valores correctos
- Asegúrate de que puedes conectarte a la base de datos

### Puertos en uso
- Usa los comandos mencionados en la sección "Verificar Puertos"
- Alternativamente, puedes cambiar los puertos en `serverless.yml`:
```yaml
custom:
  serverless-offline:
    httpPort: 3000
    lambdaPort: 3002
```

### Problemas con las dependencias de Python
- Asegúrate de que el entorno virtual está activado
- Reinstala las dependencias:
```bash
pip install -r requirements.txt
```

## Despliegue

El despliegue a AWS se realiza automáticamente a través de GitHub Actions cuando se hace push a la rama principal.

## Contribuir

1. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
2. Realiza tus cambios
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

