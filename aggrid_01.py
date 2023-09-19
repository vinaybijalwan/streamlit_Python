## modules
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

##function 
@st.cache
def data_upload():
    df = pd.read_csv('PAH_2016.csv', encoding='latin1')
    return df

df = data_upload()
#st.dataframe(data=df)


st.header("This is AgGrid Table")

AgGrid(df)