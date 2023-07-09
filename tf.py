import streamlit as st
import hydralit_components as hc

option_data = [
   {'icon': "", 'label':i} for i in ['Activity', 'Correlation', 'Literature References', 'PPI', 'Download']]

over_theme = {'txc_inactive': 'white','menu_background':'teal','txc_active':'black','option_active':'white'}
font_fmt = {'font-class':'h3','font-size':'50%'}


def tf_page():

   st.info('Information Here...')

   page = hc.option_bar(
        option_definition=option_data,
        title='',
        override_theme=over_theme,
        horizontal_orientation=True
        )
   
   if page == 'Activity':
      st.info('Activity Here')
   
   elif page == 'Correlation':
      st.info('Correlation Here')
   
   elif page == 'Literature References':
      st.info('References Here')

   elif page == 'PPI':
      st.info('PPI Here')

   elif page == 'Download':
      st.info('Download Here')