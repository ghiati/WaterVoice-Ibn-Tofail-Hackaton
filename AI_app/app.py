# api.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from langchain_groq import ChatGroq
from langchain_core.tools import Tool
from langchain_google_community import GoogleSearchAPIWrapper
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Load environment variables and initialize external tools only once at startup
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

@app.get("/generate_report")
async def generate_report():
    # Get the current month and year
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().year

    # Create a prompt with a specific time frame for the search
    research_prompt = f"""
    Find the latest news articles on water scarcity in Morocco from {current_month} {current_year}. 
    Provide a comprehensive overview of the recent developments, focusing on causes, impacts, and potential solutions 
    discussed in news released this month.
    """

    # Perform the Google search and get recent results
    try:
        search_results = tool.run(research_prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error performing Google search: {e}")

    # Define a detailed prompt for the model to generate a full report using the search results
    report_prompt = f"""
    Based on the latest information gathered from Google search results, generate a comprehensive report on water scarcity in Morocco. The report should include the following sections:

    1. **Introduction**: Provide an overview of water scarcity, explaining its significance globally and why it’s especially pressing in Morocco.

    2. **Background**: Describe the historical and geographic context of water resources in Morocco, including climate, population growth, and economic activities that affect water availability.

    3. **Causes**: Detail the main causes of water scarcity in Morocco, such as climate change, droughts, groundwater overuse, agricultural practices, and urbanization.

    4. **Current Impacts**: Explain the impacts of water scarcity on Morocco’s economy, agriculture, society, and environment, using specific examples or statistics if possible.

    5. **Latest Developments and News**: Summarize the latest news and developments on water scarcity in Morocco based on the following information:
    {search_results}

    6. **Potential Solutions**: Outline potential solutions and recommendations to mitigate water scarcity in Morocco, including both short-term and long-term strategies like water conservation, infrastructure improvements, desalination, and sustainable agriculture.

    7. **Conclusion**: Summarize the importance of addressing water scarcity in Morocco and encourage action from relevant stakeholders.

    Generate this report in a formal tone, suitable for readers seeking an in-depth understanding of the issue.
    """

    # Invoke the model with the report prompt
    try:
        response = model.invoke(report_prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating report: {e}")

    # Return the generated report
    return {"report": response}

