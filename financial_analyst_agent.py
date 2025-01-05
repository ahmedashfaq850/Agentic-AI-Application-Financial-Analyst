from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os 
from dotenv import load_dotenv
load_dotenv


# first check if API Key is set or not
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not set in environment variables")

# set api key in terminal
#export GROQ_API_KEY="your-api-key"

# Web Search Agent

web_search_agent = Agent(
    name = "web_search_agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ['Always include sources'],
    show_tools_calls = True,
    markdown = True,
    debug_mode=True
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


# Multi Agent
multi_agent = Agent(
    name="Multi Agent",
    team=[web_search_agent, finance_agent],
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Print the response
multi_agent.print_response("Tell me about the stocks of Tesla and Also tell me about the company", stream=True)