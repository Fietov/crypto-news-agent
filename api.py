from fastapi import FastAPI
from agent.crypto_agent import CryptoAgent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Crypto Agent API +++"}

@app.get("/report")
def get_report():
    agent = CryptoAgent(limit=5)
    report = agent.run()
    return report

@app.get("/report/{coin}")
def get_report_coin(coin:str):
    agent = CryptoAgent(limit=5, currencies = [coin])
    report = agent.run()
    return report