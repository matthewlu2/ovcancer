import streamlit as st
import hydralit_components as hc
from PIL import Image


def spatial_page():

   st.info('Information Here...')   
   first, middle, last = st.columns([.2, .6, .2])
   col1, col2, col3 = st.columns(3)

   IMG_REPO = 'data/website_spatial_autocorrelation'
   

   
   

   file = open('data/textfiles/website_spatial_autocorrelation.txt', 'r')
   list = file.read().splitlines()

   option = middle.selectbox(
   'Gene of Interest',
   (list))

   img = f'{IMG_REPO}/{option}.png'
   col2.image(img)

