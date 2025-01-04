from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
load_dotenv()

#A simple agent which uses DuckDuckGo to search for information

web_search_agent = Agent(
    name ="Web search agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


web_search_agent.print_response("Whats happening in France?")
