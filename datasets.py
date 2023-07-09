import streamlit as st
import hydralit_components as hc
import pandas as pd
from PIL import Image


option_data = [
   {'icon': "", 'label':i} for i in ['Metadata', 'Visualization', 'Expression']]

over_theme = {'txc_inactive': 'white','menu_background':'teal','txc_active':'black','option_active':'white'}
font_fmt = {'font-class':'h3','font-size':'50%'}

BACKGROUND_COLOR = 'white'
COLOR = 'black'


def datasets_page():

   IMG_REPO = 'data/website_feature_by_gene'
   IMG_REPO2 = 'data/website_violin'

   st.title("Table S1. Sample and Data Information")
   st.info('In this study, we combined inhouse data with 3 deposited single-cell RNA sequencing (scRNA-seq) dataset. The integrated scRNA-seq dataset consists of high-grade serous ovarian carcinoma (HGSOC) samples from 20 treatment-naïve patients. We also analyzed a spatial transcriptomics (ST) dataset which consists of HGSOC samples from 11 treatment-naïve patients, and the TCGA-OV dataset (n=248).')

  
   table = pd.read_csv("./data/tables1.csv")
   st.write(table)

   page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True
        )
   
   if page == 'Visualization':
      img1 = "./website_umap_by_group/author.png"
      img2 = "./website_umap_by_group/sample_author.png"
      img3 = "./website_umap_by_group/celltype3.png"

      st.image([img1, img2, img3], width = 350)

   elif page == 'Expression':
      
      file = open('data/textfiles/website_feature_by_gene_violin.txt', 'r')
      list = file.read().splitlines()

      option = st.selectbox(
      'Please select what grpah you want to see!',
      (list))

      img = f'{IMG_REPO}/{option}.png'
      img2 = f'{IMG_REPO2}/{option}.png'
      st.image([img, img2], caption = ['Feature Plot', 'Violin Plot'], width = 400) 

 