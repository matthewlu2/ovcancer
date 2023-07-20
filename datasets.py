import streamlit as st
import hydralit_components as hc
import pandas as pd
import os

from PIL import Image


option_data = [
   {'icon': "", 'label':i} for i in ['Metadata', 'Visualization', 'Spatial Feature Plots']]

over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'white','option_active':'teal'}
font_fmt = {'font-class':'h2','font-size':'50%'}

BACKGROUND_COLOR = 'white'
COLOR = 'black'


def datasets_page():

   st.info('In this study, we combined inhouse data with 3 deposited single-cell RNA sequencing (scRNA-seq) dataset. The integrated scRNA-seq dataset consists of high-grade serous ovarian carcinoma (HGSOC) samples from 20 treatment-naïve patients. We also analyzed a spatial transcriptomics (ST) dataset which consists of HGSOC samples from 11 treatment-naïve patients, and the TCGA-OV dataset (n=248).')
   page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True,
        )
   

   IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/ov_data/main/website_feature_by_gene/'
   IMG_REPO2 = 'https://raw.githubusercontent.com/matthewlu2/ov_data/main/website_violin/'
   IMG_REPO3 = 'data/website_spatial_feature'

   if page == 'Metadata':

      table = pd.read_csv("./data/tables1.csv")
      st.write(table)
      st.caption("Expand columns if needed")   


   elif page == 'Visualization':

      
      a, b, c = st.columns(3)

      img1 = "./data/website_umap_by_group/author.png"
      img2 = "./data/website_umap_by_group/sample_author.png"
      img3 = "./data/website_umap_by_group/celltype3.png"

      a.image(img1)
      b.image(img2)
      c.image(img3)



      file = open('data/textfiles/long_list.txt', 'r')
      list = file.read().splitlines()
      print(len(list))

      option = st.selectbox(
      'Gene of Interest',
      (list)) 

      col1, col2 = st.columns(2, gap = "large")

      img4 = f'{IMG_REPO}/{option}.png'
      img5 = f'{IMG_REPO2}/{option}.png'

      col1.image(img4, caption = 'Feature Plot')
      for i in range(12):
         col2.write("")
      col2.image(img5, caption = 'Violin Plot')
    

  

     # st.image([img1, img2, img3], width = 350)
     
   elif page == 'Spatial Feature Plots':

      #first, middle, last = st.columns([.2, .6, .2])
    

      file = open('data/textfiles/website_spatial_feature.txt', 'r')
      list = file.read().splitlines()

      option = st.selectbox(
      'Gene of Interest',
      (list))

      col1, col2, col3 = st.columns([.1, .8, .1])

      img = f'{IMG_REPO3}/{option}.png'
      col2.image(img)
 