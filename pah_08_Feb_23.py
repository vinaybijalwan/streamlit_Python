#Create Interactive Dashboards with Streamlit and Python
#Dated: 08-02-2023


#Import Libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt



## basic set up of Dashboad page

st.set_page_config(
    page_title="Patient Dashboard 2016-2022",
    page_icon="✅",
    layout="wide",
)

## load data

@st.experimental_memo
def load_data():
    data=pd.read_csv(r'PAH_2016_2022.csv', encoding='latin1', low_memory=False)
    return data

df = load_data()


# dashboard title
st.title("Patient Dashboard 2016-2022")


#Top-level filter

# top-level filters
##category of Disease filter
category_filter = st.selectbox("Select the category of Disease", pd.unique(df["Category"]))

##category_filter = st.selectbox("Select the category of Disease", pd["Category"].value_counts())

##Department wise filter
department_filter = st.selectbox("Select the Department", pd.unique(df["Department"]))


# dataframe filter
df_cat = df[df["Category"] == category_filter]

df_department = df[df["Department"] == department_filter]



