from fastapi.responses import JSONResponse
from terapias.app.shared.utils.constants import *

def success_response(status_code: int, message: str, data):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": status_code,
            "message": message,
            "data": data
        }
    )

def error_response(status_code: int, message: str, detail_errors: str = ""):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": status_code,
            "message": message,
            "data": {
                "detail_errors": detail_errors
            }
        }
    )
