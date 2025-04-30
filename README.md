# Knee Rehabilitation App Backend

Backend service for the Knee Rehabilitation Application built with FastAPI and deployed using Serverless Framework.

## Project Structure

```
knee-rehab-app-back/
├── app/                    
│   ├── api/               
│   ├── core/             
│   ├── db/                
│   ├── models/            
│   ├── services/          
│   └── main.py            
├── tests/                 
├── .venv                 
├── .gitignore            
├── handler.py            
├── requirements.txt      
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
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
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

