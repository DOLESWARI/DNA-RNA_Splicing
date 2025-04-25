import streamlit as st
import base64

# List of research papers with titles and file paths
research_papers = [
    {"title": "Paper 1: Exploring RNA Sequencing", "file": "papers/paper1.pdf"},
    {"title": "Paper 2: Advances in Splice Detection", "file": "papers/paper2.pdf"},
    {"title": "Paper 3: Machine Learning in IVF Analysis", "file": "papers/paper3.pdf"},
    {"title": "Paper 4: RNA-Seq Applications in Livestock", "file": "papers/paper4.pdf"},
    {"title": "Paper 5: Genomics in Embryo Development", "file": "papers/paper5.pdf"}
]


def display_pdf(pdf_path):
    # Read and encode the PDF in base64
    with open(pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()
        base64_pdf = base64.b64encode(pdf_data).decode('utf-8')  # Encode in base64

    # Provide a download button
    st.download_button(
        label="Download this paper",
        data=pdf_data,
        file_name=pdf_path.split("/")[-1],
        mime="application/pdf"
    )

    # Render the PDF in an iframe
    st.markdown(
        f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
        width="700" height="900" type="application/pdf"></iframe>
        """,
        unsafe_allow_html=True
    )


def main():
    st.title("Research Papers")
    st.write("Select a research paper from the list below to read or download:")

    selected_paper = st.selectbox("Available Papers", [paper["title"] for paper in research_papers])

    # Find the corresponding file path for the selected paper
    selected_file = next(
        paper["file"] for paper in research_papers if paper["title"] == selected_paper
    )

    # Display the PDF viewer
    st.write(f"You selected: **{selected_paper}**")

    # Show download button before the preview
    display_pdf(selected_file)


if __name__ == "__main__":
    main()
