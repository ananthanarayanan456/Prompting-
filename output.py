from typing import List, Dict, Any

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class Summary(BaseModel):
    summary: str = Field(description="Summary")
    facts: List[str] = Field(
        description="""
                          Generate a summary and identify two interesting facts about a person using their LinkedIn profile. 
                          Include their professional background, skills, achievements, and personal interests, 
                          then explain two standout facts"""
    )

    def ans(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}


class IceBreaker(BaseModel):
    ice_breakers: List[str] = Field(
        description="""Create Personalized ice breakers based on a person's LinkedIn activity, including posts, comments, and endorsements. 
    Ensure relevance and positivity, explaining their connection to the person's engagements"""
    )

    def ans(self) -> Dict[str, Any]:
        return {"ice_breakers": self.ice_breakers}


class TopicOfInterest(BaseModel):
    topics_of_interest: List[str] = Field(
        description="""Identify Topics that might interest a person based on their professional background, skills, and personal interests from their LinkedIn profile. """
    )

    def ans(self) -> Dict[str, Any]:
        return {"topics_of_interest": self.topics_of_interest}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
ice_breaker_parser = PydanticOutputParser(pydantic_object=IceBreaker)
topics_of_interest_parser = PydanticOutputParser(pydantic_object=TopicOfInterest)
