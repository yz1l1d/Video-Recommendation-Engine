from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Post, User
from app.utils.external_api import get_all_posts, get_all_users

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

def insert_users(db: Session):
    users = get_all_users()  # Get users from external API

    # Normalize emails & remove duplicates from API response
    seen_emails = set()
    unique_users = []
    for user in users:
        email = user["email"].strip().lower()  # Normalize email (strip spaces, lowercase)
        
        if email in seen_emails:
            print(f"⚠️ Skipping duplicate email in API response: {email}")
            continue  # Avoid duplicate processing

        seen_emails.add(email)
        unique_users.append(user)

    # Fetch all existing emails from DB (normalized)
    existing_emails = {email[0].strip().lower() for email in db.query(User.email).all()}  

    new_users = []
    for user in unique_users:
        email = user["email"].strip().lower()

        if email in existing_emails:
            print(f"⚠️ Skipping existing email in DB: {email}")
            continue  # Skip already inserted users

        new_users.append(User(
            id=user["id"],
            username=user["username"],
            email=email,  # Store normalized email
            full_name=user.get("full_name", "")
        ))
        
        existing_emails.add(email)  # Prevent duplicates in this session

    if new_users:
        try:
            db.bulk_save_objects(new_users)  # Bulk insert new users
            db.commit()
            print(f"✅ Inserted {len(new_users)} new users.")
        except Exception as e:
            db.rollback()
            print(f"❌ Error inserting users: {e}")
    else:
        print("✅ No new users to insert.")

def insert_posts(db: Session):
    posts = get_all_posts()
    existing_post_ids = {post_id[0] for post_id in db.query(Post.id).all()}  # Optimize lookup
    
    new_posts = []
    for post in posts:
        if post["id"] in existing_post_ids:
            print(f"⚠️ Skipping existing post ID: {post['id']}")
            continue

        new_posts.append(Post(
            id=post["id"],
            title=post["title"],
            content=post["content"],
            category=post["category"]
        ))
    
    if new_posts:
        db.bulk_save_objects(new_posts)
        db.commit()
        print(f"✅ Inserted {len(new_posts)} new posts.")
    else:
        print("✅ No new posts to insert.")

def insert_data():
    db = SessionLocal()
    insert_users(db)
    insert_posts(db)
    db.close()
    print("✅ Data successfully inserted!")

if __name__ == "__main__":
    insert_data()
