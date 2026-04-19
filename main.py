import os
from dotenv import load_dotenv
from agent.crypto_agent import CryptoAgent
from telegram_bot.message import TelegramBot

load_dotenv()

agent = CryptoAgent()
report = agent.run()
agent.save_report(report)

# Telegram part
bot = TelegramBot()
bot.send_report(report)

print("\n" + "="*50)
print(f" CRYPTO MARKET REPORT")
print(f" Generated at: {report.generated_at}")
print(f" Total articles analyzed: {report.total_articles}")
print("="*50)

print("\n COIN SUMMARY:")
for coin in report.coins:
    print(f"\n  {coin.coin}:")
    print(f"    Total articles : {coin.total_articles}")
    print(f"    Positive       : {coin.positive}")
    print(f"    Negative       : {coin.negative}")
    print(f"    Neutral        : {coin.neutral}")
    print(f"    Overall        : {coin.overall_sentiment.value}")