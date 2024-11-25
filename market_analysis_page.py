import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import GoogleSerperAPIWrapper

import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv("API_KEY")

# Access the environment variables
serpe_api_key = os.getenv("SERPER_API_KEY")


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    api_key= api_key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)


def market_analysis_page():
    if "user_info" not in st.session_state:
        st.warning("Please fill out the business form first.")
        return

    user_info = st.session_state["user_info"]
    st.title("Market Analysis Engine")

    def get_trending_topics(Business_specs):
        llm = model

        template = """
        Analyze these business specs and identify Keyword to be searched 
        in web for identifying opertunities:\nBusiness specs:  {business}
        \nOutput Keyword
        Note: Give only one high preority keyword"""

        prompt = ChatPromptTemplate.from_template(template)

        keyword_chain = prompt | llm | StrOutputParser()

        Search_term = keyword_chain.invoke({"business":Business_specs})

        search = GoogleSerperAPIWrapper(serper_api_key = serpe_api_key)

        search_result = search.run(f"top 5 trending topics in {Search_term} today.")

        topics = model.invoke(f"""
                              Give the below content as bulleted points, 
                              content: {search_result}""").content

        return topics


    # Simulated trend analysis function
    def analyze_trends(user_info):
        topic_data = get_trending_topics(user_info)

        trends = topic_data

        # Analyze trends using Gemini Flash
        prompt = ChatPromptTemplate.from_template("""Analyze these trends and identify opportunities:\nTrends: {trends}
                                          \nBusiness Context: {business}\nOutput actionable insights.""")

        chain = prompt | model | StrOutputParser()

        insights = chain.invoke({"trends": trends,
                                 "business": user_info["industry"]
                                 } )
        
        return trends, insights

    # Display trends and insights
    trends, insights = analyze_trends(user_info)
    st.subheader("Real-time Market Trends")
    st.write(trends)
    st.subheader("Insights and Opportunities")
    st.session_state["market_analysis_page"] = insights
    st.write(insights)
