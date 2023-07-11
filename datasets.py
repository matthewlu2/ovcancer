import streamlit as st
import hydralit_components as hc
import pandas as pd
from PIL import Image


option_data = [
   {'icon': "", 'label':i} for i in ['Metadata', 'Visualization', 'Expression', 'Feature Plots']]

over_theme = {'txc_inactive': 'white','menu_background':'teal','txc_active':'black','option_active':'white'}
font_fmt = {'font-class':'h2','font-size':'50%'}

BACKGROUND_COLOR = 'white'
COLOR = 'black'


def datasets_page():

   page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True,
        )
   

   IMG_REPO = 'data/website_feature_by_gene'
   IMG_REPO2 = 'data/website_violin'
   IMG_REPO3 = 'data/website_spatial_feature'

   if page == 'Metadata':

      st.info('In this study, we combined inhouse data with 3 deposited single-cell RNA sequencing (scRNA-seq) dataset. The integrated scRNA-seq dataset consists of high-grade serous ovarian carcinoma (HGSOC) samples from 20 treatment-naïve patients. We also analyzed a spatial transcriptomics (ST) dataset which consists of HGSOC samples from 11 treatment-naïve patients, and the TCGA-OV dataset (n=248).')
      table = pd.read_csv("./data/tables1.csv")
      st.write(table)
      st.caption("Expand columns if needed")   


   elif page == 'Visualization':

      a, b, c = st.columns(3)

      img1 = "./website_umap_by_group/author.png"
      img2 = "./website_umap_by_group/sample_author.png"
      img3 = "./website_umap_by_group/celltype3.png"

      a.image(img1)
      b.image(img2)
      c.image(img3)

  

     # st.image([img1, img2, img3], width = 350)

   elif page == 'Expression':
      first, middle, last = st.columns([.2, .6, .2])
      col1, col2 = st.columns(2, gap = "medium")

     

      file = open('data/textfiles/website_feature_by_gene_violin.txt', 'r')
      list = file.read().splitlines()

      option = middle.selectbox(
      'Please select what graph you want to see!',
      (list))

      img = f'{IMG_REPO}/{option}.png'
      img2 = f'{IMG_REPO2}/{option}.png'

      # st.image(img, caption = 'Feature Plot', width = 400)
      # st.image(img2, caption = 'Violin Plot', width = 400)

      col1.image(img, caption = 'Feature Plot')
      col2.image(img2, caption = 'Violin Plot')
     
   elif page == 'Feature Plots':

      first, middle, last = st.columns([.2, .6, .2])
      col1, col2, col3 = st.columns(3)

      file = open('data/textfiles/website_spatial_feature.txt', 'r')
      list = file.read().splitlines()

      option = middle.selectbox(
      'Please select what graph you want to see!',
      (list))

      img = f'{IMG_REPO3}/{option}.png'
      col2.image(img)
 