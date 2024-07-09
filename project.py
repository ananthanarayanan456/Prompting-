from typing import Tuple
from linkedin_look import look as linkedin_agent
from custom import get_ice_breaker_chain, get_interests_chain, get_summary_chain

from linkedin import scrape_linkedin_profile
from output import Summary, IceBreaker, TopicOfInterest


def idea(
    name: str,
) -> Tuple[Summary, TopicOfInterest, IceBreaker, str]:

    linkedin_username = linkedin_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_chain = get_summary_chain()
    summary_and_facts: Summary = summary_chain.invoke(
        input={"information": linkedin_data},
    )

    interests_chain = get_interests_chain()
    interests: TopicOfInterest = interests_chain.invoke(
        input={"information": linkedin_data}
    )

    ice_breaker_chain = get_ice_breaker_chain()
    ice_breakers: IceBreaker = ice_breaker_chain.invoke(
        input={"information": linkedin_data}
    )

    return (
        summary_and_facts,
        interests,
        ice_breakers,
        linkedin_data.get("profile_pic_url"),
    )


if __name__ == "__main__":
    print(idea("Anantha Narayanan"))
