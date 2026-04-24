import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from models.news import NewsArticle, Sentiment
from dotenv import load_dotenv
from config import config


load_dotenv()

class NewsAnalyzer:

    def __init__(self):
        # LLM connection
        self.llm = ChatGroq(
            api_key = config.groq_api_key,
            model_name = config.default_model
        )

        self.prompt = PromptTemplate(
            input_variables = ["title", "description"],
            template = """
            You are a crypto market analyst. Analyze this news article and respond in this EXACT format:

            SENTIMENT: [POSITIVE or NEGATIVE or NEUTRAL]
            COINS: [ONLY return coin ticker symbols like BTC,ETH,XRP. If no specific coin ticker is mentioned return NONE. Never return text explanations.]
            REASON: [one sentence explaining market impact]

            News Title: {title}
            News Description: {description}

            Your analysis:
            
            """

        )

        #Connecting prompts and llm with a chain
        self.chain = self.prompt | self.llm

    def analyze(self, article: NewsArticle) -> NewsArticle:
        try:
            # send article to llm
            result = self.chain.invoke({
                "title": article.title,
                "description": article.description or "No description"
            })

            # LLM responce line by line
            response_text = result.content
            lines = response_text.strip().split("\n")

            for line in lines:
                # Extracting sentiment
                if line.startswith("SENTIMENT:"):
                    sentiment_value = line.replace("SENTIMENT:", "").strip()
                    try:
                        article.sentiment = Sentiment(sentiment_value.lower())
                    except:
                        article.sentiment = Sentiment.NEUTRAL

                # Extracting coins
                elif line.startswith("COINS:"):
                    coins_raw = line.replace("COINS:", "").strip()
                    if coins_raw != "NONE":
                        article.coins_mentioned = [c.strip().upper() for c in coins_raw.split(",")]
        except Exception as e:
            print(f"⚠️ Analysis failed for article: {article.title[:50]} — {e}")
            article.sentiment = Sentiment.NEUTRAL

        return article

