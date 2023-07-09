import streamlit as st
import hydralit_components as hc
from PIL import Image

option_data = [
   {'icon': "", 'label':i} for i in ['Autocorrelation', 'Feature Plots']]

over_theme = {'txc_inactive': 'white','menu_background':'teal','txc_active':'black','option_active':'white'}
font_fmt = {'font-class':'h3','font-size':'50%'}


def spatial_page():

   IMG_REPO = 'data/website_spatial_autocorrelation'
   IMG_REPO2 = 'data/website_spatial_feature'

   st.info('Information Here...')
   
   page = hc.option_bar(
      option_definition=option_data,
      title='',
      override_theme=over_theme,
      horizontal_orientation=True
      )
   
   if page == 'Autocorrelation':
      
      file = open('data/textfiles/website_spatial_autocorrelation.txt', 'r')
      list = file.read().splitlines()

      option = st.selectbox(
      'Please select what grpah you want to see!',
      (list))

      img = f'{IMG_REPO}/{option}.png'
      st.image(img, width = 400)

   elif page == 'Feature Plots':

      file = open('data/textfiles/website_spatial_feature.txt', 'r')
      list = file.read().splitlines()

      option = st.selectbox(
      'Please select what grpah you want to see!',
      (list))

      img = f'{IMG_REPO2}/{option}.png'
      st.image(img, width = 400)