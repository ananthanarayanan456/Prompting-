from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

import os

from output import summary_parser, ice_breaker_parser, topics_of_interest_parser

os.environ["OPENAI_API_KEY"]=""

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
creative = ChatOpenAI(temperature=0.9, model="gpt-3.5-turbo")


def get_summary_chain() -> RunnableSequence:
    summary_template = """
        Using detailed LinkedIn {information}, generate a comprehensive summary and identify two interesting facts about a person. 
        Requirements: Summarize their professional background, educational qualifications, key skills, industry experience, career progression, and professional goals. 
        Identify unique achievements, unusual skills or experiences, personal interests, impactful contributions, and notable endorsements. 
        Procedure: Extract detailed data from the LinkedIn profile, analyze it to identify patterns and highlights, and compose a concise, engaging summary. 
        Identify and explain standout facts that enhance the understanding of the person's unique attributes.
           
        Output: A well-crafted summary paragraph and two compelling, brief facts.
         \n{format_instructions}
     """

    summary = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    return summary | llm | summary_parser


def get_interests_chain() -> RunnableSequence:
    interesting_facts_template = """
         Given comprehensive LinkedIn {information}, identify three topics that might interest a person based on their professional background, skills, and personal interests. 
         Requirements: For professional interests, focus on industry trends, career development, and technical skills. 
         For personal interests, consider hobbies, volunteering, and personal development. 
         For networking, look at industry events, thought leaders, and professional associations. 
         Procedure: Extract detailed data from their LinkedIn profile, analyze it to identify relevant patterns and highlights, and identify topics of interest based on professional, personal, and networking aspects. 

         Output: Provide detailed topics of interest, each with an explanation of its relevance.

        \n{format_instructions}
     """

    interesting_facts_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": topics_of_interest_parser.get_format_instructions()
        },
    )

    return interesting_facts_prompt_template | llm | topics_of_interest_parser


def get_ice_breaker_chain() -> RunnableSequence:
    ice_breaker_template = """
        Given comprehensive LinkedIn {information}, create two creative ice breakers derived from the person's activity. 
        Requirements: Analyze their posts, shared articles, comments, group activities, followed pages, endorsements, and recommendations. 
        Ensure ice breakers are relevant to their activity, engaging, and positive to spark meaningful conversations. 
        Procedure: Extract and analyze detailed LinkedIn activity data to understand their interests and professional focus, identify notable patterns or themes, 
        and develop personalized ice breakers based on this analysis. 
        
        Output: Provide two detailed and personalized ice breakers with explanations of their relevance and connection to the person's LinkedIn engagements.
        \n{format_instructions}
     """

    ice_breaker_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )

    return ice_breaker_prompt_template | llm | ice_breaker_parser
