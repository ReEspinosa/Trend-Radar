from fastapi import APIRouter
from app.services.trends_service import get_trending_now, get_monthly_calendar

router = APIRouter()

@router.get("/now")
def trending_now():
    return get_trending_now()

@router.get("/calendar")
def monthly_calendar():
    return get_monthly_calendar()