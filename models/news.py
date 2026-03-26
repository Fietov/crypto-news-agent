# 1 have to import all required tools
from pydantic import BaseModel, field_validator, HttpUrl
from enum import Enum
from datetime import datetime

# 2 Sentiment - doesn't matter first or second, well it does matter cuse we gonna call it in news class
class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"

# 3 News filter using pydantic library with the basemodel class, here we have to define what we need to get and what type of data
class NewsArticle(BaseModel):
    title: str
    description: str | None = None
    published_at: datetime
    coins_mentioned: list[str] = []
    sentiment: Sentiment | None = None
    kind: str

    @field_validator('coins_mentioned')
    @classmethod

    def coins_upper(cls, coins: list[str]) -> list[str]:
        result = []
        for coin in coins:
            result.append(coin.upper())
        return result



# 4 add ON for coins mentioned so we get them with uppercase