import streamlit as st
import hydralit_components as hc
from PIL import Image

def interaction_page():

   IMG_REPO = 'data/website_interaction'

   file = open('data/textfiles/website_interaction.txt', 'r')
   list = file.read().splitlines()

   option = st.selectbox(
   'Please select what dotplot you want to see!',
   (list))

   img1 = f'{IMG_REPO}/{option}_immune.png'
   img2 = f'{IMG_REPO}/{option}_nonimmune.png'
   st.image([img1, img2], caption = ['Immune', 'Nonimmune'], width = 400)







   


 
       

   