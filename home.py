import streamlit as st
from PIL import Image

def run():
    # Title and Introduction
    st.title("DNA Processes: Helicase, Bonds, and Gene Expression")
    st.write("Explore the fascinating world of DNA, focusing on helicase, DNA structure, and the steps of gene expression including transcription, translation, and splicing.")

    # Section: DNA Helicase
    st.header("What is DNA Helicase?")
    st.write("DNA helicase is an essential enzyme that unwinds the double helix of DNA during replication. It breaks the hydrogen bonds between the complementary bases, enabling other enzymes to replicate each strand.")

    # Section: Bonds in DNA
    st.header("Bonds in DNA Structure")
    st.write("The DNA molecule consists of two main types of bonds:")
    st.markdown("- **Hydrogen Bonds**: These occur between the nitrogenous bases (A-T with 2 hydrogen bonds, G-C with 3 hydrogen bonds).\n- **Phosphodiester Bonds**: These connect the sugar-phosphate backbone of the DNA strand.")

    # Load and display an image of DNA structure
    dna_image = Image.open("images/image_6.jpg")  # Replace with the path to your image
    st.image(dna_image, caption="DNA Structure Showing Hydrogen and Phosphodiester Bonds", use_container_width=True)

    # Section: Gene Expression Processes
    st.header("Gene Expression: Transcription, Splicing, and Translation")
    st.subheader("Transcription")
    st.write("During transcription, RNA polymerase synthesizes messenger RNA (mRNA) from the DNA template strand.")

    # Load and display a transcription flowchart
    transcription_image = Image.open("images/img_2.png")  # Replace with the path to your image
    st.image(transcription_image, caption="Transcription Flowchart", use_container_width=True)

    st.subheader("Splicing")
    st.write("After transcription, the pre-mRNA undergoes splicing to remove introns and join exons, forming a mature mRNA strand ready for translation.")

    # Load and display a splicing diagram
    splicing_image = Image.open("images/img_1.png")  # Replace with the path to your image
    st.image(splicing_image, caption="Splicing Diagram", use_container_width=True)

    st.subheader("Translation")
    st.write("Translation is the process where ribosomes synthesize proteins using the sequence encoded in mRNA.")

    # Load and display a translation process diagram
    translation_image = Image.open("images/img_4.png")  # Replace with the path to your image
    st.image(translation_image, caption="Translation Diagram", use_container_width=True)

    # Section: Interactive Elements (Expanded)
    st.header("Explore Further")
    st.write("Use the slider below to choose a step in gene expression for more details:")
    step = st.slider("Select Step", 1, 3, 1, format="Step %d")

    if step == 1:
        st.subheader("Step 1: Transcription")
        st.write("Transcription is the first step of gene expression where a particular segment of DNA is copied into RNA by the enzyme RNA polymerase. It involves three stages:")
        st.markdown("- **Initiation**: RNA polymerase binds to the promoter region of DNA.\n- **Elongation**: RNA polymerase synthesizes a complementary RNA strand.\n- **Termination**: RNA polymerase detaches upon reaching a termination sequence.")
        transcription_detail_image = Image.open("images/img_1.png")  # Replace with your image
        st.image(transcription_detail_image, caption="Detailed Transcription Process", use_container_width=True)

    elif step == 2:
        st.subheader("Step 2: Splicing")
        st.write("Splicing occurs after transcription to remove non-coding sequences (introns) from the pre-mRNA. The remaining coding sequences (exons) are joined together to form mature mRNA. Key components involved in splicing include:")
        st.markdown("- **Spliceosome**: A complex of RNA and proteins that facilitates splicing.\n- **Exons and Introns**: Exons are expressed sequences, while introns are non-coding regions.")
        splicing_detail_image = Image.open("images/img_3.jpg")  # Replace with your image
        st.image(splicing_detail_image, caption="Detailed Splicing Process", use_container_width=True)

    elif step == 3:
        st.subheader("Step 3: Translation")
        st.write("Translation converts the sequence of mRNA into a specific protein. This process occurs in the ribosome and involves:")
        st.markdown("- **Initiation**: The ribosome assembles around the mRNA and the first tRNA.\n- **Elongation**: Amino acids are added one by one to the growing peptide chain.\n- **Termination**: The ribosome releases the completed protein upon reaching a stop codon.")
        translation_detail_image = Image.open("images/img_2.png")  # Replace with your image
        st.image(translation_detail_image, caption="Detailed Translation Process", use_container_width=True)

    st.write("\nDive deeper into the fascinating mechanisms of gene expression with the detailed visuals and descriptions provided above. Each step is a critical part of life’s central dogma!")

# Ensure compatibility with main script
if __name__ == "__main__":
    run()