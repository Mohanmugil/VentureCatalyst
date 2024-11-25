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

def simulate_customer_journey(user_info):
    # Create a prompt template for simulating the customer journey
    template = """
    Based on the customer details provided below, simulate a typical customer journey:
    
    Industry: {industry}
    Target Audience: {target_audience}
    Pain Points: {pain_points}
    Product Features: {product_features}
    Product Benefits: {product_benefits}
    
    Steps:
    1. Describe how a customer will first interact with the product.
    2. What actions will they take to understand the value proposition?
    3. Identify any obstacles or challenges in the journey.
    4. Suggest improvements to enhance the user experience.
    """
    
    prompt = ChatPromptTemplate.from_template(template)

    # Initialize LLM model
    llm = model
    journey_simulation_chain = prompt | llm | StrOutputParser()

    journey_simulation = journey_simulation_chain.invoke({"industry": user_info['industry'],
                                                          "target_audience": user_info['target_audience'],
                                                          "pain_points": user_info['pain_points'],
                                                          "product_features": user_info['product_features'],
                                                          "product_benefits": user_info['product_benefits']
                                                          } )
    
    return journey_simulation

# Example usage
def customer_journey_section():
    if "customer_discovery_info" not in st.session_state:
        st.warning("Please fill out the customer discovery form first.")
        return
    
    user_info = st.session_state["customer_discovery_info"]
    st.header("Customer Journey Simulation")
    
    # Simulate customer journey
    journey_simulation = simulate_customer_journey(user_info)

    st.session_state["customer_journey_section"] = journey_simulation
    
    st.subheader("Customer Journey Simulation")
    st.write(journey_simulation)
