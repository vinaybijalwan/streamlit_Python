#Create Interactive Dashboards with Streamlit and Python
#Dated: 09-02-2023


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
    page_title="Patient Dashboard 2022",
    page_icon="✅",
    layout="wide",
)

## load data

@st.experimental_memo
def load_data():
    data=pd.read_csv(r'PAH_April_2022.csv', encoding='latin1', low_memory=False)
    return data

df = load_data()

# dashboard title
st.title("Patient Dashboard April -2022")


#Top-level filter

# top-level filters
##category of Disease filter
#category_filter = st.selectbox("Select the category of Disease", pd.unique(df["Category"]))


with st.sidebar:
    category_filter = st.selectbox("Select the category of Disease", pd.unique(df["Category"]))
    department_filter  = st.selectbox("Select the Department", pd.unique(df["Department"]))




# dataframe filter
df_cat = df[df["Category"] == category_filter]

df_department = df[df["Department"] == department_filter]


# create three columns
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

# fill in those three columns with respective metrics or KPIs
kpi1.metric(
    label="Patient ⏳",
    value=len(df),
    #delta=round(df_cat) - 10,
)


#Count the number of unique values in a specific column
kpi2.metric(
    label="Doctor's ⏳",
    value=df['Vaidya Name'].nunique(),
    #delta=round(df_cat) - 10,
)

##Total Department in Hospital
kpi3.metric(
    label="Department ⏳",
    value=df['Department'].nunique(),
    #delta=round(df_cat) - 10,
)

kpi4.metric(
    label="Disease ⏳",
    value=df['Disease'].nunique(),
    #delta=round(df_cat) - 10,
)

