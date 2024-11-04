# config.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.tools import Tool

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not set in the environment.")

model = ChatGroq(groq_api_key=groq_api_key, model="llama-3.1-70b-versatile")
search = GoogleSearchAPIWrapper()
tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)
