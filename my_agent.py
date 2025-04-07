
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro",
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature=0.4,
)

def ask_agent(user_query: str) -> str:
    messages = [HumanMessage(content=user_query)]
    response = llm.invoke(messages)
    return response.content
