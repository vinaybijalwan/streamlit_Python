#Create Interactive Dashboards with Streamlit and Python
#Dated: 10-02-2023


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
st.header("Patient Dashboard April -2022")


#Top-level filter

# top-level filters
##category of Disease filter
#category_filter = st.selectbox("Select the category of Disease", pd.unique(df["Category"]))


#with st.sidebar:
#    category_filter = st.selectbox("Select the category of Disease", pd.unique(df["Category"]))
#    department_filter  = st.selectbox("Select the Department", pd.unique(df["Department"]))


# dataframe filter
#df_cat = df[df["Category"] == category_filter]

#df_department = df[df["Department"] == department_filter]

##This is Add on dated 10 Feb 2023
 


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


st.subheader("Patient Filter Data")
with st.sidebar:
    column_options = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", column_options)
    unique_values = df[selected_column].unique().tolist()
    selected_value = st.selectbox("Select a value to filter by", unique_values)
    filtered_df = df[df[selected_column] == selected_value]


st.write('Total patient    ', selected_value, '  ', len(filtered_df))

st.dataframe(filtered_df)




