from config import config
import requests
from models.report import Report

class TelegramBot:

    def __init__(self):
        self.token = config.telegram_bot_token
        self.chat_id = config.telegram_chat_id
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, text: str) -> None:
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": text}
        response = requests.post(url, json=payload)
        return response.json()

    def send_report(self, report: Report) -> None:
        message = f"CRYPTO MARKET REPORT\n"
        message += f"Generated at: {report.generated_at}\n"
        message += f"Total articles analyzed: {report.total_articles}\n"
        message += "COIN SUMMARY:\n"

        for coin in report.coins:
            message += f"\n{coin.coin}:\n"
            message += f"Total articles : {coin.total_articles}\n"
            message += f"Overall: {coin.overall_sentiment.value}"

            self.send_message(message)



