import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = (
    "sk-proj-UJ85WX1YennKvtYgZxgnT3BlbkFJ37Zx90buCyvPCpdFh9Wv"
)

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai.chat_models.base import ChatOpenAI


def get_profile_url(name: str):
    """Searches for Linkedin or twitter Profile Page"""
    search = TavilySearchAPIWrapper()
    result = TavilySearchResults(api_wrapper=search)
    res = result.run(f"{name}")
    return res


def LinkReturn(companyName):
    res = []
    for i in get_profile_url(companyName):
        res.append(i["url"])
    return res


# if __name__=="__main__":
#     print(LinkReturn("Ankur warikoo"))

# tool = TavilySearchResults()
# print(tool.invoke({"query": f"Give me LinkedIn profile of Anantha Narayanan"}))

instructions = """You are an assistant."""

base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)
llm = ChatOpenAI(temperature=0)

tavily_tool = TavilySearchResults()

tools = [tavily_tool]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

# print(agent_executor.invoke({"input": "How is Anantha Narayanan and check from linkedin?"}))


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]
