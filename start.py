import streamlit as st
import hydralit_components as hc
from PIL import Image
import pandas as pd

from datasets import datasets_page
from tf import tf_page
from interaction import interaction_page
from spatial import spatial_page
from home import home_page

st.set_page_config(
        page_title='Ovarian Cancer',
        page_icon= "./logos/ovcancer.png",
        initial_sidebar_state="expanded",
)


max_width_str = f"max-width: {85}%;"
st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
        unsafe_allow_html=True,
    )

Image.MAX_IMAGE_PIXELS = None

HOME = "Home"
DATASET = "Datasets"
TF = "Transcription Factors"
INTERACTION = "Ligand-receptor Interaction"
SPATIAL = "On Spatial"


tabs = [
    HOME,
    DATASET,
    TF,
    INTERACTION,
    SPATIAL,
]


option_data = [
   {'icon': "🏠", 'label':HOME},
   {'label':DATASET},
   {'label':TF},
   {'label':INTERACTION},
   {'label':SPATIAL},  
   # to do logo have {'icon': "(emoji)" 'label':____}, 
]

theme = {'txc_inactive': 'white','menu_background':'teal','txc_active':'black'}
chosen_tab = hc.nav_bar(menu_definition=option_data, override_theme = theme, use_animation= bool(True), hide_streamlit_markers= bool(True))


if chosen_tab ==HOME:
    home_page()

elif chosen_tab == DATASET:
    datasets_page()

elif chosen_tab == TF:
    tf_page()

elif chosen_tab == INTERACTION:
    interaction_page()

elif chosen_tab == SPATIAL:
    spatial_page()