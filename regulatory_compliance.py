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

def regulatory_compliance_guidance(user_info):
    # Create a prompt template for regulatory compliance
    template = """
    Based on the provided details, suggest the key regulatory and legal requirements for expanding into the target international market.
    
    Industry: {industry}
    Product Type: {product_type}
    Target Region: {target_region}
    
    Provide:
    1. Key regulatory requirements for market entry
    2. Legal considerations for operating in the target region
    3. Recommendations for ensuring compliance
    """

    prompt = ChatPromptTemplate.from_template(template)

    # Initialize LLM model
    llm = model

    compliance_guidance_chain = prompt | llm | StrOutputParser()

    compliance_guidance = compliance_guidance_chain.invoke({
                "target_region": user_info['target_region'],
                "industry": user_info['industry'],
                "product_type": user_info['product_type']
            })
    
    return compliance_guidance

# Example usage
def regulatory_compliance_section():
    if "market_expansion_info" not in st.session_state:
        st.warning("Please fill out the market expansion form first.")
        return
    
    user_info = st.session_state["market_expansion_info"]
    st.header("Regulatory Compliance Guidance")
    
    # Provide regulatory compliance insights
    compliance_guidance = regulatory_compliance_guidance(user_info)

    st.session_state["regulatory_compliance_section"] = compliance_guidance
    
    st.subheader("Regulatory Compliance Insights")
    st.write(compliance_guidance)
