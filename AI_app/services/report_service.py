# services/report_service.py
from datetime import datetime
from config import model, tool
from langchain_core.output_parsers import StrOutputParser
from utils.prompt_templates import get_report_prompt ,get_research_prompt
parser = StrOutputParser()

async def generate_report():
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().year
    
    research_prompt = get_research_prompt(current_month, current_year)
    search_results = tool.run(research_prompt)

    report_prompt = get_report_prompt(current_month,current_year,search_results)

    chain = model | parser
    return {"report": chain.invoke(report_prompt)}
