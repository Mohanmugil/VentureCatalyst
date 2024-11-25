import streamlit as st

# Import pages
from user_info_page import user_info_page
from market_analysis_page import market_analysis_page
from customer_discovery_page import customer_discovery_page
from market_expansion_page import market_expansion_page
from Download_pdf import download_pdf_report_section

# Add a logo in the sidebar
st.sidebar.image("Logo.png", 
                 width=200)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["User Information", "Market Analysis", "Customer Discovery", "Market Expansion", "Download Report"])

# Page routing

if page == "User Information":
    user_info_page()
elif page == "Market Analysis":
    market_analysis_page()
elif page == "Customer Discovery":
    customer_discovery_page()
elif page == "Market Expansion":
    market_expansion_page()
elif page == "Download Report":
    download_pdf_report_section()


