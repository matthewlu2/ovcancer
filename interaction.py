import streamlit as st
import hydralit_components as hc
from PIL import Image

def interaction_page():
   
   #st.info('Information Here...')  
   #first, middle, last = st.columns([.2, .6, .2])
   

   IMG_REPO = 'data/website_interaction'

   file = open('data/textfiles/website_interaction.txt', 'r')
   list = file.read().splitlines()

   option = st.selectbox(
   'Please select what dotplot you want to see!',
   (list))

   col1, col2 = st.columns(2, gap = "medium")

   img1 = f'{IMG_REPO}/{option}_immune.png'
   img2 = f'{IMG_REPO}/{option}_nonimmune.png'

   col1.image(img1, caption = 'Immune')
   col2.image(img2, caption = 'Nonimmune')

   #st.image([img1, img2], caption = ['Immune', 'Nonimmune'], width = 400)







   


 
       

   