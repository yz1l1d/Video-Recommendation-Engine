from fastapi import APIRouter
from app.utils.external_api import (
    get_viewed_posts,
    get_liked_posts,
    get_inspired_posts,
    get_rated_posts,
    get_all_posts,
    get_all_users,
)

router = APIRouter()

@router.get("/viewed")
def viewed_posts():
    """Fetch all viewed posts"""
    return get_viewed_posts()

@router.get("/liked")
def liked_posts():
    """Fetch all liked posts"""
    return get_liked_posts()

@router.get("/inspired")
def inspired_posts():
    """Fetch all inspired posts"""
    return get_inspired_posts()

@router.get("/rated")
def rated_posts():
    """Fetch all rated posts"""
    return get_rated_posts()

@router.get("/posts")
def all_posts():
    """Fetch all posts"""
    return get_all_posts()

@router.get("/users")
def all_users():
    """Fetch all users"""
    return get_all_users()
