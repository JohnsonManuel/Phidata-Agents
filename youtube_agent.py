
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.youtube_tools import YouTubeTools
from phi.tools.googlesearch import GoogleSearch

from dotenv import load_dotenv

# Loading the environment variables
import os
load_dotenv()

google_search_agent = Agent(
    tools=[GoogleSearch()],
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
    ],
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    debug_mode=True,
)

youtube_agent = Agent(
    name ="YouTube agent",
    role="You are an YouTube agent that is used to fetch the captions of a YouTube video and retun key points.",
    tools=[YouTubeTools()],
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
)

youtube_agent.print_response("Create a blog post from the video https://www.youtube.com/watch?v=4LeBTYpfgS4 in 300 words", markdown=True)
