from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Video, User

# Create tables (if not already created)
Base.metadata.create_all(bind=engine)

# Insert sample data
def insert_sample_data():
    db: Session = SessionLocal()

    # Add users
    users = [
        User(username="test_user"),
        User(username="john_doe"),
        User(username="jane_smith"),
    ]

    # Add videos
    videos = [
        Video(title="Motivational Video 1", category="Motivation", url="http://example.com/video1", likes=100, views=500),
        Video(title="Success Story", category="Success", url="http://example.com/video2", likes=80, views=400),
        Video(title="Mindset Shift", category="Growth", url="http://example.com/video3", likes=120, views=700),
    ]

    db.add_all(users)
    db.add_all(videos)
    db.commit()
    db.close()

if __name__ == "__main__":
    insert_sample_data()
    print("Sample data inserted successfully!")
 