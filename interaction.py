import streamlit as st
import hydralit_components as hc
# from github import Github
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





   # st.info('Information Here...')
   
   # my_git = Github("_______")
   # IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/ov_interaction/main/'


   # repo = my_git.get_repo("matthewlu2/ov_interaction")
   # contents = repo.get_contents("")
   # list = []
   # count = 0
   # for content_file in contents:
   #    text = str(content_file.path)
   #    end = text.index('_')
   #    substring = text[0:end]
   #    list.append(substring)

   # list = set(list)

  
   # option = st.selectbox(
   # 'Please select what dotplot you want to see!',
   # (list))

   # img1 = f'{IMG_REPO}/{option}_immune.png'
   # img2 = f'{IMG_REPO}/{option}_nonimmune.png'
   # st.image([img1, img2], caption = ['Immune', 'Nonimmune'], width = 400)

   


 
       

   