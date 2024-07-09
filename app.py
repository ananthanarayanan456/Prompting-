import streamlit as st
from dotenv import load_dotenv
from project import idea

load_dotenv()

st.title("Research Project")

st.write("Enter a name to get information:")

name = st.text_input("Name: ")

# st.write("Enter a Company Name to get information:")

# company=st.text_input("Company: ")

if st.button("Process"):
    if name:
        summary_and_facts, interests, ice_breakers, profile_pic_url = idea(name=name)

        st.subheader("Profile Picture")
        if profile_pic_url:
            st.image(profile_pic_url, caption=name)

        st.subheader("Summary")
        val = summary_and_facts.ans()
        st.write(val["summary"])

        st.subheader("Facts")
        # for i in range(len(val)):
        st.write(val["facts"][0])

        st.subheader("Interests")
        val = interests.ans()
        # for i in range(len(val)):
        #     st.write(val["topics_of_interest"][i])

        st.write(interests.ans())

        st.subheader("Ice Breakers")
        val = ice_breakers.ans()
        st.write(val["ice_breakers"])

    else:
        st.error("Please enter a name.")


if __name__ == "__main__":
    pass
