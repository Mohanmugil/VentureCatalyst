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

def assess_cultural_compatibility(user_info):
    # Create a prompt template for cultural compatibility
    template = """
    Based on the provided details, assess whether the product is culturally compatible with the target market. Consider language, values, and buying behaviors in the region.
    
    Industry: {industry}
    Product Type: {product_type}
    Target Region: {target_region}
    Target Customers: {target_customers}
    
    Provide:
    1. Assessment of cultural compatibility
    2. Any potential cultural barriers
    3. Suggestions for adapting the product to the market
    """

    prompt = ChatPromptTemplate.from_template(template)

    # Initialize LLM model
    llm = model

    cultural_assessment_chain = prompt | llm | StrOutputParser()

    cultural_assessment = cultural_assessment_chain.invoke({
                "target_region": user_info['target_region'],
                "industry": user_info['industry'],
                "product_type": user_info['product_type'],
                "target_customers": user_info['target_customers']
            })
    
    return cultural_assessment

# Example usage
def cultural_compatibility_section():
    if "market_expansion_info" not in st.session_state:
        st.warning("Please fill out the market expansion form first.")
        return
    
    user_info = st.session_state["market_expansion_info"]
    st.header("Cultural Compatibility Assessment")
    
    # Assess cultural compatibility
    cultural_assessment = assess_cultural_compatibility(user_info)

    st.session_state["cultural_compatibility_section"] = cultural_assessment
    
    st.subheader("Cultural Compatibility Insights")
    st.write(cultural_assessment)
