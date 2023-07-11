import streamlit as st
import hydralit_components as hc
from PIL import Image

def interaction_page():
   
   st.info('Information Here...')  

   col1, col2, col3 = st.columns(3, gap = "medium")

   IMG_REPO = 'data/website_interaction'

   file = open('data/textfiles/website_interaction.txt', 'r')
   list = file.read().splitlines()

   option = col1.selectbox(
   'Please select what dotplot you want to see!',
   (list))


   img1 = f'{IMG_REPO}/{option}_immune.png'
   img2 = f'{IMG_REPO}/{option}_nonimmune.png'

   col2.image(img1, caption = 'Immune')
   col3.image(img2, caption = 'Nonimmune')

   #st.image([img1, img2], caption = ['Immune', 'Nonimmune'], width = 400)







   


 
       

   