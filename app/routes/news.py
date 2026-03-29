from fastapi import APIRouter
from app.services.news_service import get_today_news, get_yesterday_news

router = APIRouter()

@router.get("/today")
def today_news():
    return get_today_news()

@router.get("/yesterdasy")
def yesterday_news():
    return get_yesterday_news()