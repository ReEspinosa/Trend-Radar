from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes import news, trends, calendar

app = FastAPI(title="Trend Radar API")
templates = Jinja2Templates(directory="app/templates")

app.include_router(news.router, prefix="/news", tags=["News"])
app.include_router(trends.router, prefix="/trends", tags=["Trends"])
app.include_router(calendar.router, prefix="/calendar", tags=["Calendar"])

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})