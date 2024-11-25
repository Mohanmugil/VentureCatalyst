import streamlit as st
from fpdf import FPDF
import pypandoc

pypandoc.download_pandoc()


# Function to create a docx
def create_docx(markdown_content, filename="overall_report.docx"):
    # Convert Markdown to docx
    try:
        pypandoc.convert_text(
            markdown_content,
            to='docx',
            format='md',
            outputfile=filename
        )
        st.success(f"Report successfully created: {filename}")
    except RuntimeError as e:
        st.error(f"Error in Report generation: {e}")
# Streamlit UI
# st.write("Provide a list of strings below:")


def download_pdf_report_section():
    if "market_expansion_info" not in st.session_state:
        st.warning("Please fill out All the forms first.")
        return
    
    # Input list of strings
    insights = st.session_state["market_analysis_page"] 
    customer_discovery  = st.session_state["customer_discovery_section"] 
    journey_simulation = st.session_state["customer_journey_section"]
    international_market = st.session_state["international_market_section"]
    cultural_compatibility = st.session_state["cultural_compatibility_section"]
    regulatory_compliance = st.session_state["regulatory_compliance_section"]
    localized_growth_strategy = st.session_state["localized_growth_strategy_section"]

    markdown_strings = [insights, 
                    customer_discovery, 
                    journey_simulation, 
                    international_market, 
                    cultural_compatibility,
                    regulatory_compliance,
                    localized_growth_strategy
                    ]
    
    st.title("Download Overall Report")

    if st.button("Generate report"):
        if markdown_strings:
            # Join the strings into a single document
            strings_content = "\n\n".join(markdown_strings)
            
            # Generate PDF
            docx_filename = "overall_report.docx"
            create_docx(strings_content, docx_filename)

            # Provide download link
            with open(docx_filename, "rb") as docx_file:
                st.download_button(
                    label="Download Document",
                    data=docx_file,
                    file_name="overall_report.docx",
                    mime="application/docx",
                )
        else:
            st.warning("Please fill out All the forms first.")
