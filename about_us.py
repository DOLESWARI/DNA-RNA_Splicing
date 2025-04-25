import streamlit as st


def run():
    st.title("Welcome to Brain Tumor Insight")
    st.write(
        "This platform is designed to help users explore advanced tools and insights related to brain tumor classification and research.")

    # Features Section
    st.header("Features of the App")
    st.markdown("""
    - **Prediction of Brain Tumors**: Upload medical imaging or genomic data to receive predictions using state-of-the-art models.
    - **RNA-Seq Analysis (IVF)**: Analyze RNA sequencing data for in-vitro fertilization insights.
    - **DNA Analysis**: Gain insights into genetic markers and their role in brain tumor development.
    - **Research Papers**: Access curated research papers on brain tumors and related topics.
    - **Feedback**: Provide valuable feedback to help us improve.
    """)

    # Instructions Section
    st.header("How to Use")
    st.markdown("""
    1. Use the sidebar to navigate between different features.
    2. For prediction tasks, prepare your data in the required format and upload it.
    3. Explore research papers and learn about recent advancements in the field.
    """)

    # Motivation Section
    st.header("Our Mission")
    st.write("""
    At Brain Tumor Insight, we aim to bridge the gap between cutting-edge research and accessible tools 
    for professionals and enthusiasts alike. Together, we can better understand and combat brain tumors.
    """)

    # Contact Information
    st.header("Contact Us")
    st.write("For queries or support, feel free to reach out to us at:")
    st.write("📧 **Email**: support@braintumorinsight.com")
    st.write("🌐 **Website**: [www.braintumorinsight.com](https://www.braintumorinsight.com)")
