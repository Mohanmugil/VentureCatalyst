import streamlit as st

# Collect customer discovery-related details
def customer_discovery_form():
    st.title("Customer Discovery Module")

    with st.form("customer_discovery_form"):
        st.subheader("Tell us about your target customers")
        industry = st.text_input("Industry (E.g. Technology, Healthcare, Education, Other)")
        target_audience = st.text_input("Target Audience (e.g., Age, Gender, Interests)")
        pain_points = st.text_area("Customer Pain Points")
        product_features = st.text_area("Key Features of Your Product")
        product_benefits = st.text_area("Benefits of Your Product")
        validation_methods = st.text_area("How do you plan to validate your product?")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.session_state["customer_discovery_info"] = {
                "industry": industry,
                "target_audience": target_audience,
                "pain_points": pain_points,
                "product_features": product_features,
                "product_benefits": product_benefits,
                "validation_methods": validation_methods,
            }
            st.success("Customer Discovery information saved!")
