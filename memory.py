import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_core.embeddings import Embeddings
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

embeddings: Embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

vector_store = SupabaseVectorStore(
    client=supabase,
    table_name="memory",
    embedding=embeddings,
    query_name="match_documents"  # Optional
)
