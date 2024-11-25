import streamlit as st
from customer_discovery_form import customer_discovery_form
from icp_and_need_mapping import customer_discovery_section
from customer_journey_simulation import customer_journey_section

def customer_discovery_page():
    st.title("Customer Discovery Module")
    
    # Collect user input if not collected already
    customer_discovery_form()
    
    # Display ICP and Need Mapping insights
    customer_discovery_section()
    
    # Simulate Customer Journey
    customer_journey_section()
