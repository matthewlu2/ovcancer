import streamlit as st
import hydralit_components as hc
from PIL import Image
import streamlit_analytics

def home_page():

    streamlit_analytics.start_tracking()
    streamlit_analytics.stop_tracking()
    
    img = "./data/figure1.png"

    st.markdown("<h2 style='text-align: center;  color: Black;'>Single-cell analysis reveals the stromal dynamics and tumor-specific characteristics in the microenvironment of ovarian cancer</h1>", unsafe_allow_html=True)
    st.image(img)
    st.markdown('Read our paper here: https://www.biorxiv.org/content/10.1101/2023.06.07.544095v1')    
    st.write('High-grade serous ovarian carcinoma (HGSOC) is a heterogeneous disease, and a high stromal/desmoplastic tumor microenvironment (TME) is associated with a poor outcome. Stromal cell subtypes, including fibroblasts, myofibroblasts, and cancer-associated mesenchymal stem cells, establish a complex network of paracrine signaling pathways with tumor-infiltrating immune cells that drive effector cell tumor immune exclusion and inhibit the antitumor immune response. Single-cell transcriptomics of the HGSOC TME from public and in-house datasets revealed a distinct transcriptomic landscape for immune and non-immune cells in high-stromal vs. low-stromal tumors. High-stromal tumors had a lower fraction of certain T cells, natural killer (NK) cells, and macrophages and increased expression of CXCL12 in epithelial cancer cells and cancer-associated mesenchymal stem cells (CA-MSCs). Analysis of cell-cell communication indicated that epithelial cancer cells and CA-MSCs secreted CXCL12 that interacted with the CXCR4 receptor, which was overexpressed on NK and CD8+ T cells. CXCL12 and/or CXCR4 antibodies confirmed the immunosuppressive role of CXCL12-CXCR4 in high-stromal tumors.')
