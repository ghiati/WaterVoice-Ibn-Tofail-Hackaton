# utils/prompt_templates.py

def get_report_prompt(current_month, current_year, search_results):
    return f"""
    Generate a monthly update report on water scarcity in Morocco, based on the latest news and developments from Google search results for {current_month} {current_year}. The report should cover the following sections:

    1. **Recent Causes**: Identify any new or significant causes of water scarcity highlighted in recent news, focusing on changes or events unique to this period.

    2. **Latest Impacts**: Describe the recent impacts of water scarcity reported this month on Morocco’s economy, agriculture, society, and environment. Provide specific examples, statistics, or incidents covered in the latest news.

    3. **Updated Potential Solutions**: Outline any newly proposed solutions or updates to existing strategies that could help mitigate water scarcity, as discussed in the current news. Emphasize both short-term and long-term strategies relevant to this month’s findings.

    4. **Summary of Key Updates**: Briefly summarize the critical developments and emphasize any urgent actions suggested by experts or policymakers in response to the latest situation.

    Use the following recent search results as the basis for this report:
    {search_results}

    Write the report in a formal tone, suitable for readers who are familiar with the water scarcity issue but seek the latest updates.
    """

def get_research_prompt(current_month, current_year):
    return f"""
    Search for the latest news articles on water scarcity in Morocco published in {current_month} {current_year}. Focus on finding recent developments, with particular attention to:

    1. New or emerging causes of water scarcity reported this month.
    2. Recent impacts of water scarcity on Morocco’s economy, agriculture, society, and environment.
    3. Newly proposed or updated solutions discussed in response to the latest situation.

    Provide an overview that highlights these aspects specifically, so the report will reflect the latest news and expert insights from this period.
    """


def get_quiz_prompt():
    return """
    Create 5 multiple-choice questions based on recent information about water scarcity in Morocco.
    Each question should have:
    - A question text
    - Four answer choices labeled A, B, C, and D
    - One correct answer
    Format the response in JSON with question text, choices, and correct answer.
    """
