# Crypto News AI Agent

An Ai Agent that fetches real time crypto news from cryptopanic api and analyzes market sentiment using LLM.

## Function
- Fetches latest news about crypto from CryptoPanic API
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
3. Create '.env' file with your OWN API keys 
    ```
    CRYPTOPANIC_API_KEY=your_key
    GROQ_API_KEY=your_key
    LANGSMITH_API_KEY=your_key
    LANGSMITH_TRACING=true
    LANGSMITH_PROJECT=Crypto_Agent
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
```