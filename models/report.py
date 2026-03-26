from pydantic import BaseModel
from datetime import datetime
from models.news import NewsArticle, Sentiment

class CoinSummary(BaseModel):
    coin: str
    total_articles: int
    positive: int = 0
    negative: int = 0
    neutral: int = 0
    overall_sentiment: Sentiment | None = None

class Report(BaseModel):
    generated_at: datetime
    total_articles: int
    coins: list[CoinSummary] = []
    articles: list[NewsArticle] = []