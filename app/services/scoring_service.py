from datetime import datetime

VIRAL_KEYWORDS = {
    "alto": ["trump", "ia", "inteligencia artificial", "openai", "apple", "guerra", "crisis",
             "demanda", "filtración", "hack", "censura", "despidos", "escándalo"],
    "medio": ["samsung", "google", "meta", "nasa", "elon", "android", "iphone",
              "récord", "nuevo", "lanzamiento", "actualización"],
    "bajo": ["análisis", "review", "comparativa", "guía", "oferta", "descuento"]
}

RECURRING_TOPICS = {
    3: ["día de la mujer", "8 de marzo", "feminismo", "género", "igualdad"],
    4: ["tierra", "medio ambiente", "clima", "sostenibilidad"],
    6: ["pride", "lgbtq", "diversidad"],
    9: ["regreso a clases", "educación", "universidades"],
    11: ["buen fin", "black friday", "ofertas"],
    12: ["año nuevo", "navidad", "retrospectiva"]
}

def score_article(article: dict) -> dict:
    score = 0.0
    title = (article.get("title") or "").lower()
    description = (article.get("description") or "").lower()
    text = title + " " + description

    # Score por keywords
    for word in VIRAL_KEYWORDS["alto"]:
        if word in text:
            score += 3.0

    for word in VIRAL_KEYWORDS["medio"]:
        if word in text:
            score += 1.5

    for word in VIRAL_KEYWORDS["bajo"]:
        if word in text:
            score -= 0.5

    # Bonus si el tema es recurrente este mes
    current_month = datetime.utcnow().month
    recurring = RECURRING_TOPICS.get(current_month, [])
    is_recurring = False
    for word in recurring:
        if word in text:
            score += 2.0
            is_recurring = True

    article["score"] = round(score, 2)
    article["is_recurring"] = is_recurring
    return article

def score_and_sort(articles: list) -> list:
    scored = [score_article(a) for a in articles]
    return sorted(scored, key=lambda x: x["score"], reverse=True)