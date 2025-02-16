from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Video, UserInteraction

router = APIRouter()

@router.get("/feed")
def get_feed(username: str, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch top 10 most viewed videos (basic recommendation)
    recommended_videos = db.query(Video).order_by(Video.views.desc()).limit(10).all()

    return {"user": username, "recommended_videos": [{"id": v.id, "title": v.title, "url": v.url} for v in recommended_videos]}
