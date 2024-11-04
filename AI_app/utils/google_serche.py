# utils/google_search.py
from langchain_google_community import GoogleSearchAPIWrapper

def search_google(query: str):
    search = GoogleSearchAPIWrapper()
    return search.run(query)
