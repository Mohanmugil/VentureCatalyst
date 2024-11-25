import streamlit as st

# Collect market expansion-related details
def market_expansion_form():
    st.title("Market Expansion Advisor")

    with st.form("market_expansion_form"):
        st.subheader("Tell us about your market expansion plans")
        target_region = st.selectbox("Select Target Region", ["North America", "Europe", "Asia", "Africa", "Latin America", "Australia"])
        industry = st.selectbox("Industry", ["Technology", "Healthcare", "Education", "Other"])
        product_type = st.text_input("Product Type (e.g., Software, Hardware, Service)")
        target_customers = st.text_area("Target Customers (e.g., Age, Gender, Interests)")
        expansion_goals = st.text_area("What are your market expansion goals?")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.session_state["market_expansion_info"] = {
                "target_region": target_region,
                "industry": industry,
                "product_type": product_type,
                "target_customers": target_customers,
                "expansion_goals": expansion_goals,
            }
            st.success("Market Expansion information saved!")
