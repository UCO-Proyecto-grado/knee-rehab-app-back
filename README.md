# Knee Rehabilitation App Backend

Backend service for the Knee Rehabilitation Application built with FastAPI and deployed using Serverless Framework.

## Project Structure

```
knee-rehab-app-back/
├── lambda_lesiones/
│   └── main.py  ← FastAPI + Mangum
│   └── api/, models/, schemas/, services/
│
├── lambda_rehab/
│   └── main.py  ← FastAPI + Mangum
│   └── api/, models/, schemas/, services/
│
├── shared/   
│   ├── core/
│   │   ├── config.py
│   │   ├── response_handler.py 
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── session.py
│   │   ├── dependencies.py
│   │   ├── base.py
│   │   └── base_class.py
│   │
│   └── utils/
│       └── constants.py
│
├── tests/ # Pruebas unitarias del sistema
│   ├── test_rehab.py
│   ├── test_health.py
│   └── test_db.py
├── .venv
├── requirements.txt
├── .gitignore
└── serverless.yml
```

## Technologies Used

- FastAPI - Modern, fast web framework for building APIs
- SQLAlchemy - SQL toolkit and ORM
- PostgreSQL - Database
- Serverless Framework - For AWS Lambda deployment
- Mangum - AWS Lambda handler for ASGI applications

## Prerequisites

- Python 3.8+
- Node.js and npm (for Serverless Framework)
- PostgreSQL database
- AWS account (for deployment)

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install pydantic-settings
```

3. Install Serverless Framework:
```bash
npm install -g serverless
```

4. Configure environment variables:
Create a `.env` file in the root directory with the following variables:
```
DATABASE_HOST=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
```

## Development

To run the application locally:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Testing

Run tests using pytest:

```bash
pytest
```

## Deployment

Deploy to AWS using Serverless Framework:

```bash
serverless deploy
```

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License

[Your License Here]

## Contributing

[Your Contributing Guidelines Here]

