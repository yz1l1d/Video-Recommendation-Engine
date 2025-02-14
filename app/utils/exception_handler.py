from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

# Import logger from logging_config.py
from app.utils.loggin_config import logger

async def custom_exception_handler(request: Request, exc: HTTPException):
    """
    Custom exception handler to log errors and return JSON response.
    """
    logger.error(f"Error {exc.status_code}: {exc.detail}")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
