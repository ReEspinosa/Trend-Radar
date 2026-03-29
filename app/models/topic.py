from pydantic import BaseModel
from typing import Optional

class Topic(BaseModel):
    title: str
    description: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    score: Optional[float] = 0.0
    category: Optional[str] = None
    published_at: Optional[str] = None
    is_recurring: Optional[bool] = False