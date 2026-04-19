import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    # API keys
    cryptopanic_api_key: str = os.getenv("CRYPTOPANIC_API_KEY","")
    groq_api_key: str = os.getenv("GROQ_API_KEY","")
    news_data_api_key: str = os.getenv("NEWS_DATA_API_KEY","")
    telegram_bot_api_key: str = os.getenv("TELEGRAM_BOT_TOKEN","")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID","")

    # Agent Settings
    default_limit: int = 10
    default_model: str = "llama-3.3-70b-versatile"

    class Config:
        env_file = ".env"
        extra = "ignore"


# Single instance used everywhere
config = Config()
