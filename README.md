# Crypto News AI Agent

An Ai Agent that fetches real time crypto news from NewsData api and analyzes market sentiment using LLM.

## Function
- Fetches latest news about crypto from NewsData.io 
- Analyzes each article with Groq LLM (llama-3.3-70b-versatile)
- Determines the sentiment of each article whether its Positive, Negative, or Neutral
- Extracts mentioned coins
- Generates a market report by each coin
- LLM cals being tracked by langsmith

## Tech Stack
- Python, OOP
- Pydantic (data validation)
- Langchain (LLM orchestration)
- Groq (free llm api)
- Langsmith (agent monitoring)

## How to Set Up
1. Clone the repo
2. Install all the dependencies: ```pip install -r requirements.txt```
3. Create '.env' file with your OWN API keys (Project is focused only on Groq AI, if you would like to use other llm, you will need to customize it.) 
    ```
    NEWS_DATA_API=your key (new api that app supports)
    CRYPTOPANIC_API_KEY=your_key (old version of an api that app doesn's support anymore)
    GROQ_API_KEY=your_key
    LANGSMITH_API_KEY=your_key
    LANGSMITH_TRACING=true
    LANGSMITH_PROJECT=Crypto_Agent
    TELEGRAM_BOT_TOKEN=your_key (optional)
    TELEGRAM_CHAT_ID=your_key (optional)
    ```
## Setting up Telegram Bot (optional)
```
    1. Open Telegram and search for @BotFather
    2. Send `/newbot`
    3. Follow instructions to create your bot
    4. Copy the token BotFather gives you → TELEGRAM_BOT_TOKEN
    5. Send a message to your bot
    6. Visit: `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
    7. Find `"id"` inside `"chat"` → TELEGRAM_CHAT_ID
   ```
   
4. Run: ```python main.py```

## Project Structure
```
crypto_news_agent/
-- models/          # Pydantic data models
-- collectors/      # News fetching from CryptoPanic
-- analyzers/       # LLM sentiment analysis
-- agent/           # Main agent orchestration
-- config.py        # Centralized settings
-- main.py          # Entry point
-- telegram_bot     # Extracting results to the telegram (optional)
```
