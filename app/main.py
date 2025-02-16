from fastapi import FastAPI
from app.routes import data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Video Recommendation Engine!"}

app.include_router(data.router, prefix="/data", tags=["Data Collection"])
