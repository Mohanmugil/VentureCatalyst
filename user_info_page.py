import streamlit as st

def user_info_page():
    # if not st.session_state.get("logged_in"):
    #     st.warning("Please log in first.")
    #     return
    
    st.title("VentureCatalyst")
    st.subheader('AI-Powered Success for Entrepreneurs.')
    st.header("Tell Us About Your Business")
    with st.form("user_info_form"):
        business_name = st.text_input("Business Name")
        target_audience = st.text_input("Target Audience")
        industry = st.selectbox("Industry", ["Technology", "Healthcare", "Education", "Other"])
        business_description = st.text_area("A brief description about your Business.")
        current_stage = st.radio("Current Stage", ["Idea", "MVP", "Revenue Generating"])
        competitors = st.text_area("Competitors (comma-separated)")
        geo_focus = st.text_input("Geographical Focus")
        challenges = st.text_area("What are your current challenges?")
        goals = st.text_area("What do you want to achieve with this tool?")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.session_state["user_info"] = {
                "business_name": business_name,
                "target_audience": target_audience,
                "industry": industry,
                "business_description": business_description,
                "current_stage": current_stage,
                "competitors": competitors,
                "geo_focus": geo_focus,
                "challenges": challenges,
                "goals": goals,
            }
            st.success("Information saved!")
