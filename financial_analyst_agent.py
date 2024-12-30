from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()

# web search agent 
web_search_agent = Agent(
  name = "web_search_agent",
  role = "Search the Web for Financial Data",
  model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
  tools = [DuckDuckGo()],
  instructions = ["Alway include sources"],
  show_tools_calls = True,
  markdown = True,
)


# Financial Analyst Agent

financial_agent = Agent(
    name = "financial_analyst_agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True,
    )],
    instructions = ["Use always table to show data"],
    show_tools_calls = True,
    markdown = True,
)
  
    
# multi-agent

multi_ai_agent = Agent(
    team = [web_search_agent, financial_agent],
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions = ["Always include sources","Use table to display the data"],
    show_tools_calls = True,
    markdown = True, 
)
    

# Run the multi-agent
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Facebook", stream = True)