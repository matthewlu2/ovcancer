import streamlit as st
import hydralit_components as hc
from PIL import Image


def spatial_page():

   st.info('Information Here...')   
   col1, col2 = st.columns(2)

   IMG_REPO = 'data/website_spatial_autocorrelation'
   

   
   

   file = open('data/textfiles/website_spatial_autocorrelation.txt', 'r')
   list = file.read().splitlines()

   option = col1.selectbox(
   'Gene of Interest',
   (list))

   img = f'{IMG_REPO}/{option}.png'
   col2.image(img)

