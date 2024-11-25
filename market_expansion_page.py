import streamlit as st
from market_expansion_form import market_expansion_form
from market_analysis import international_market_section
from cultural_compatibility import cultural_compatibility_section
from regulatory_compliance import regulatory_compliance_section
from localized_growth_strategy import localized_growth_strategy_section

def market_expansion_page():
    market_expansion_form()
    international_market_section()
    cultural_compatibility_section()
    regulatory_compliance_section()
    localized_growth_strategy_section()
