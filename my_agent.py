from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Please check your .env file.")

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro",
    google_api_key=api_key,
    temperature=0.4,
)

def ask_agent(user_query: str) -> str:
    messages = [HumanMessage(content=user_query)]
    response = llm.invoke(messages)
    return response.content
