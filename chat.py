import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from memory import vector_store 
load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.4
)

# Conversation Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Retrieval Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector_store.as_retriever(),
    memory=memory,
    return_source_documents=True
)
