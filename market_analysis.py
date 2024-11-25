from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st

# Load the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    api_key= api_key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

def analyze_international_market(user_info):
    # Create a prompt template for market analysis
    template = """
    Based on the details below, suggest the best international markets for expansion, considering market trends, customer needs, and business potential:
    
    Industry: {industry}
    Target Region: {target_region}
    Product Type: {product_type}
    Target Customers: {target_customers}
    Expansion Goals: {expansion_goals}
    
    Provide:
    1. Suggested international markets for expansion
    2. Reasons why these markets are ideal for the business
    3. Market size and growth potential
    """

    prompt = ChatPromptTemplate.from_template(template)

    # Initialize LLM model
    llm = model

    market_analysis_chain = prompt | llm | StrOutputParser()

    market_analysis = market_analysis_chain.invoke({
                "target_region": user_info['target_region'],
                "industry": user_info['industry'],
                "product_type": user_info['product_type'],
                "target_customers": user_info['target_customers'],
                "expansion_goals": user_info['expansion_goals'],
            })
    
    return market_analysis

# Example usage
def international_market_section():
    if "market_expansion_info" not in st.session_state:
        st.warning("Please fill out the market expansion form first.")
        return
    
    user_info = st.session_state["market_expansion_info"]
    st.header("International Market Analysis")
    
    # Analyze international market opportunities
    market_analysis = analyze_international_market(user_info)

    st.session_state["international_market_section"] = market_analysis
    
    st.subheader("Market Analysis Insights")
    st.write(market_analysis)
