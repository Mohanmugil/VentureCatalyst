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

def generate_localized_growth_strategy(user_info):
    # Create a prompt template for localized growth strategy
    template = """
    Based on the provided details, suggest a localized growth strategy for entering the target region. Focus on tailoring the product, marketing, and customer experience for this market.
    
    Industry: {industry}
    Target Region: {target_region}
    Product Type: {product_type}
    Target Customers: {target_customers}
    
    Provide:
    1. Localized growth strategy
    2. Recommendations for product adaptation
    3. Suggestions for marketing tactics
    """

    prompt = ChatPromptTemplate.from_template(template)

    # Initialize LLM model
    llm = model

    growth_strategy_chain = prompt | llm | StrOutputParser()

    growth_strategy = growth_strategy_chain.invoke({
                "target_region": user_info['target_region'],
                "industry": user_info['industry'],
                "product_type": user_info['product_type'],
                "target_customers": user_info['target_customers']
            })
    
    return growth_strategy

# Example usage
def localized_growth_strategy_section():
    if "market_expansion_info" not in st.session_state:
        st.warning("Please fill out the market expansion form first.")
        return
    
    user_info = st.session_state["market_expansion_info"]
    st.header("Localized Growth Strategy")
    
    # Generate localized growth strategy
    growth_strategy = generate_localized_growth_strategy(user_info)
    
    st.session_state["localized_growth_strategy_section"] = growth_strategy
    st.subheader("Growth Strategy Insights")
    st.write(growth_strategy)
