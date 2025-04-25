import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Tuple

# Extended database for various cancers, tumors, and other diseases
disease_database = {
    "ATCG->ATGG": ("Cystic Fibrosis", True, 24),
    "GATT->GACT": ("Sickle Cell Anemia", True, 12),
    "TTAG->TTTG": ("Huntington's Disease", False, 0),
    "CGTA->AGTA": ("Breast Cancer", True, 18),
    "CCGG->CCAG": ("Thalassemia", True, 15),
    "ACGT->ACAT": ("Leukemia", True, 20),
    "TATA->TAAA": ("Parkinson's Disease", False, 0),
    "GGCC->GACC": ("Alzheimer's Disease", False, 0),
    "AGTC->AGTT": ("Colon Cancer", True, 22),
    "CTGA->CTAA": ("Pancreatic Cancer", False, 0),
    "ACTG->ACCG": ("Lung Cancer", True, 24),
    "GTAC->GTCC": ("Skin Cancer", True, 12),
    "CGAT->CTAT": ("Brain Tumor", False, 0),
    "TACG->TAGG": ("Prostate Cancer", True, 18),
    "GCAT->GCTT": ("Ovarian Cancer", True, 20),
    "TAGG->TTGG": ("Thyroid Cancer", True, 15),
    "CAGT->CATT": ("Bladder Cancer", True, 14),
    "TCCA->TAAA": ("Liver Cancer", False, 0),
    "GCTA->GATA": ("Esophageal Cancer", True, 22),
    "CCAG->CAAG": ("Gastric Cancer", False, 0)
}

curability_info = {
    True: "This disease is curable. Estimated treatment time: {} months.",
    False: "This disease is currently incurable."
}

def convert_mrna_to_dna(sequence: str) -> str:
    """Converts an mRNA sequence to its corresponding DNA sequence."""
    return sequence.replace('U', 'T')

def find_mutations(sequence: str) -> List[Tuple[str, str]]:
    """Detects possible mutations in the input DNA sequence."""
    mutations = []
    for mutation, details in disease_database.items():
        original, mutated = mutation.split('->')
        if original in sequence:
            mutations.append((mutation, details[0]))
    return mutations

def correct_sequence(sequence: str) -> str:
    """Returns the corrected DNA sequence by replacing mutations."""
    corrected_sequence = sequence
    for mutation in disease_database.keys():
        original, mutated = mutation.split('->')
        corrected_sequence = corrected_sequence.replace(original, mutated)
    return corrected_sequence

def predict_disease(mutations: List[Tuple[str, str]]) -> List[str]:
    """Predicts disease from mutations and returns curability information."""
    results = []
    if not mutations:
        results.append("No known mutations detected. The DNA sequence appears normal.")
    else:
        for mutation, disease in mutations:
            disease_info = disease_database[mutation]
            curability_message = curability_info[disease_info[1]].format(disease_info[2])
            result = f"Detected Mutation: {mutation}\nAssociated Disease: {disease}\n{curability_message}\n{'-' * 40}"
            results.append(result)
    return results

def plot_disease_summary(mutations: List[Tuple[str, str]]):
    """Displays a bar chart summarizing diseases and their curability."""
    if mutations:
        diseases = [disease_database[mutation][0] for mutation, _ in mutations]
        curable_status = [disease_database[mutation][1] for mutation, _ in mutations]
        data = {
            "Disease": diseases,
            "Curable": ["Curable" if status else "Incurable" for status in curable_status]
        }
        df = pd.DataFrame(data)
        st.bar_chart(df["Curable"].value_counts(), use_container_width=True)

def run():
    """Runs the DNA/mRNA Mutation Detector and Disease Predictor app."""
    st.title("DNA/mRNA Sequence Mutation Detector and Disease Predictor")

    input_type = st.radio("Select input type:", ("DNA", "mRNA"))
    sequence = st.text_input("Enter the sequence:", value="GATTCCGGATCGTATAGGCC")

    if st.button("Analyze Sequence"):
        if sequence:
            if input_type == "mRNA":
                sequence = convert_mrna_to_dna(sequence)
                st.markdown(f"Converted mRNA to DNA: `{sequence}`")

            mutations = find_mutations(sequence)
            results = predict_disease(mutations)
            for result in results:
                st.text(result)

            corrected_sequence = correct_sequence(sequence)
            st.markdown(f"**Corrected DNA Sequence:**")
            st.markdown(f"<mark style='background-color:green; color:white;'>{corrected_sequence}</mark>", unsafe_allow_html=True)

            plot_disease_summary(mutations)
        else:
            st.warning("Please enter a valid sequence.")

# Ensure compatibility with main script
if __name__ == "__main__":
    run()
