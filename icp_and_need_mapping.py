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

def generate_icp_and_need_mapping(user_info):
    # Create a prompt template for ICP generation and need mapping
    template = """
    You are a business strategist helping to build an ideal customer profile (ICP) and match customer needs to product features.
    Given the information below, provide a detailed ICP and map the customer needs to product features.
    
    Industry: {industry}
    Target Audience: {target_audience}
    Pain Points: {pain_points}
    Product Features: {product_features}
    Product Benefits: {product_benefits}
    
    Provide:
    1. Ideal Customer Profile (ICP)
    2. Needs Mapping (matching customer pain points with product features)
    3. Suggest methods to validate product-market fit based on these insights.
    """

    prompt = ChatPromptTemplate.from_template(template)

    # Initialize LLM model
    llm = model

    insights_chain = prompt | llm | StrOutputParser()

    insights = insights_chain.invoke({"industry": user_info['industry'],
                                      "target_audience": user_info['target_audience'],
                                      "pain_points": user_info['pain_points'],
                                      "product_features": user_info['product_features'],
                                      "product_benefits": user_info['product_benefits']
                                      } )
    
    return insights

# Example usage
def customer_discovery_section():
    if "customer_discovery_info" not in st.session_state:
        st.warning("Please fill out the customer discovery form first.")
        return
    
    user_info = st.session_state["customer_discovery_info"]
    st.header("Customer Discovery Insights")
    
    # Generate ICP and need mapping using LLM
    insights = generate_icp_and_need_mapping(user_info)

    st.session_state["customer_discovery_section"] = insights
    
    st.subheader("Ideal Customer Profile (ICP) and Needs Mapping")
    st.write(insights)