# Trend Radar

Aplicación web para monitorear tendencias y noticias en tiempo real, orientada al mercado hispanohablante. Combina datos de Google Trends y NewsAPI para mostrar los temas más relevantes del momento, con un calendario editorial de temas estacionales.

## Funcionalidades

- Feed de noticias del dia y del dia anterior, ordenadas por score de viralidad
- Calendario mensual con temas estacionales por semana
- Sistema de puntuacion de articulos basado en palabras clave virales
- Panel de notas y tareas por dia en el calendario
- Interfaz web servida directamente desde FastAPI

## Tecnologias

- Python 3
- FastAPI + Uvicorn
- Jinja2 (templates HTML)
- NewsAPI (`newsapi-python`)
- Google Trends (`pytrends`)
- Pydantic
- python-dotenv

## Estructura del proyecto
```
.
├── app/
│   ├── main.py               # Entrada de la aplicacion
│   ├── models/
│   │   └── topic.py          # Modelo de datos Topic
│   ├── routes/
│   │   ├── news.py           # Endpoints /news
│   │   ├── trends.py         # Endpoints /trends
│   │   └── calendar.py       # Endpoint /calendar
│   ├── services/
│   │   ├── news_service.py       # Logica de consulta a NewsAPI
│   │   ├── trends_service.py     # Logica de Google Trends y calendario estacional
│   │   └── scoring_service.py    # Puntuacion y ordenamiento de articulos
│   └── templates/
│       └── index.html        # Interfaz web
├── requirements.txt
└── .env
```

## Instalacion
```bash
git clone https://github.com/tu-usuario/trend-radar.git
cd trend-radar
pip install -r requirements.txt
```

Crea un archivo `.env` en la raiz del proyecto:
```
NEWS_API_KEY=tu_clave_de_newsapi
```

Puedes obtener una clave gratuita en [newsapi.org](https://newsapi.org).

## Uso
```bash
uvicorn app.main:app --reload
```

La aplicacion estara disponible en `http://localhost:8000`.

## Endpoints disponibles

| Metodo | Ruta               | Descripcion                        |
|--------|--------------------|------------------------------------|
| GET    | `/`                | Interfaz web principal             |
| GET    | `/news/today`      | Noticias de las ultimas 24 horas   |
| GET    | `/news/yesterday`  | Noticias de las ultimas 48 horas   |
| GET    | `/trends/now`      | Tendencias actuales en Google      |
| GET    | `/trends/calendar` | Calendario de temas estacionales   |
| GET    | `/calendar/`       | Endpoint de calendario (pendiente) |
