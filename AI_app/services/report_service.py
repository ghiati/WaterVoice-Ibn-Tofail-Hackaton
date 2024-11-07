# services/report_service.py
from datetime import datetime
from config import model, tool


from langchain_core.output_parsers import StrOutputParser
from utils.prompt_templates import get_report_prompt ,get_research_prompt
parser = StrOutputParser()

def generate_report():
    # Current month and year
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().year

    # Get research prompt and perform search
    research_prompt = get_research_prompt(current_month, current_year)
    search_results = tool.run(research_prompt)  # Assuming this is synchronous

    # Get report prompt and generate the report
    report_prompt = get_report_prompt(current_month, current_year, search_results)
    chain = model | parser
    report = chain.invoke(report_prompt)  # Assuming this is also synchronous

    return {"report": report}
