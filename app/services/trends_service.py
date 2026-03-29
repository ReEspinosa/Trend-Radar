from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

pytrends = TrendReq(hl='es-MX', tz=360)

# Temas que históricamente se vuelven virales cada mes
SEASONAL_TOPICS = {
    1:  ["año nuevo propósitos", "dietas enero", "reyes magos"],
    2:  ["san valentín", "día del amor", "14 de febrero"],
    3:  ["día de la mujer", "8 de marzo", "primavera", "semana santa"],
    4:  ["día de la tierra", "impuestos", "semana santa"],
    5:  ["día de las madres", "10 de mayo", "mayo"],
    6:  ["día del medio ambiente", "verano", "world cup"],
    7:  ["vacaciones verano", "calor extremo"],
    8:  ["regreso a clases", "útiles escolares", "back to school"],
    9:  ["independencia mexico", "15 de septiembre", "informe gobierno"],
    10: ["halloween", "día de muertos", "octubre rosa"],
    11: ["día de muertos", "buen fin", "black friday"],
    12: ["navidad", "año nuevo", "posadas"]
}

def get_trending_now(keywords: list = ["inteligencia artificial", "política mexico", "tecnología"]):
    try:
        pytrends.build_payload(keywords[:5], timeframe='now 7-d', geo='MX')
        data = pytrends.interest_over_time()
        if data.empty:
            return {}
        return data.tail(1).to_dict(orient='records')[0]
    except Exception as e:
        return {"error": str(e)}

def get_monthly_calendar():
    current_month = datetime.utcnow().month
    current_year = datetime.utcnow().year
    seasonal = SEASONAL_TOPICS.get(current_month, [])

    weeks = []
    for week_num in range(1, 5):
        weeks.append({
            "week": week_num,
            "label": f"Semana {week_num} de {current_month}/{current_year}",
            "seasonal_topics": seasonal,
            "trending_score": "alto" if week_num in [2, 3] else "medio"
        })

    return {
        "month": current_month,
        "year": current_year,
        "weeks": weeks
    }