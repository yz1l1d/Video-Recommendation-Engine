from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Video Recommendation Engine!"}

@app.get("/feed")
def get_feed(username: str):
    return {"message": f"Feed for {username}"}
