from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base
from app.database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String)
    url = Column(String, unique=True)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)

class UserInteraction(Base):
    __tablename__ = "user_interactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    video_id = Column(Integer, ForeignKey("videos.id"))
    interaction_type = Column(String)  # viewed, liked, rated, etc.
    score = Column(Float, default=0)
