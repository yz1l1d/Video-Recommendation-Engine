from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Video Recommendation Engine"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


from app.utils.loggin_config import logger
logger.info("Server started successfully!")
logger.error("An error occurred!")

from fastapi import FastAPI
from app.utils.exception_handler import custom_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# Register custom exception handlers
app.add_exception_handler(StarletteHTTPException, custom_exception_handler)
app.add_exception_handler(RequestValidationError, custom_exception_handler)
