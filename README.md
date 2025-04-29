# DNA-RNA_Splicing
This project focuses on analyzing DNA sequences to predict possible splicing patterns that contribute to gene expression through RNA transcription and translation. The tool takes DNA sequences as input, identifies intron and exon regions, simulates RNA splicing, and outputs the final mRNA sequence that could be translated into proteins. The project is particularly useful for understanding gene regulation, alternative splicing, and identifying potential markers related to genetic diseases or conditions like tumors and cancer.

## Features
Accepts DNA sequences from users as input.

Identifies exons and introns using predefined biological markers or machine learning models.

Performs in-silico splicing to remove introns and generate mature mRNA.

Optionally, translates the spliced mRNA into a protein sequence using codon tables.

Can highlight mutations or anomalies that may lead to diseases (e.g., cancer markers).

Visual representation of the splicing process (if implemented with a GUI or web interface).

## Motivation
RNA splicing plays a crucial role in post-transcriptional gene regulation. Errors in splicing mechanisms are known to lead to several diseases, including cancer. This project aims to model and simulate the biological splicing process computationally, allowing researchers and students to visualize and analyze genetic data efficiently.

![Splicing Screenshot](https://raw.githubusercontent.com/DOLESWARI/DNA-RNA_Splicing/main/Screenshot%20(154).png)

## Technologies Used
Python for core logic and sequence manipulation

Biopython for biological sequence handling

Machine Learning (optional) for classification of exons/introns

Matplotlib or Plotly for visualizations (if implemented)

Streamlit for web integration

## Disclaimer
This project is for educational and research purposes only. It is not intended for clinical or diagnostic use.
