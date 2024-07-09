import os

from langchain import hub

from langchain.agents import create_react_agent, AgentExecutor

from langchain_community.tools.tavily_search import TavilySearchResults

from langchain_core.tools import Tool
from langchain_openai.chat_models.base import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate

from dotenv import load_dotenv
from tool import get_profile_url_tavily


load_dotenv()
os.environ["OPENAI_API_KEY"]=""


def look(name: str) -> str:

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    template = """Given the full name {name_of_person}, 
                 provide the URL to their LinkedIn profile page. 
                 Your response should only contain the URL
                 """

    prompt = PromptTemplate(
        template=template,
        input_variables=["name_of_person"],
    )
    tools = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need get the linkedIn page URL",
        ),
    ]

    react = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=react,
    )

    exe = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )

    result = exe.invoke(input={"input": prompt.format_prompt(name_of_person=name)})

    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == "__main__":
    print(look("Karan Rai launch ventures"))
