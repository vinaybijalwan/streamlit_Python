import pandas as pd
import streamlit as st
import plotly_express as px
from PIL import Image

st.set_page_config(page_title='patient 2022')

st.header('Patient Report 2022')

st.subheader('Report in Streamlit')


##load data
csv_file = 'PAH_2022.csv'
sheet_name = 'PAH_2022'