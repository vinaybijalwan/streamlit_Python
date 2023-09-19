import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development



## basic set up of Dashboad page
st.set_page_config(
    page_title="Real-Time Data Patient Dashboard",
    page_icon="✅",
    layout="wide",
)

##load data set from CSV file

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv('PAH_2016.csv', encoding='latin1', low_memory=False)


df = get_data()


# dashboard title
st.title("Real-Time / Live Data Patient Dashboard")


# top-level filters
gender_filter = st.sidebar.selectbox("Select the Gender", pd.unique(df["Gender"]))
state_filter = st.sidebar.selectbox("Select the State", pd.unique(df["State"]))

# dataframe filter
df_gender = df[df["Gender"] == gender_filter]
df_state = df[df["State"] == state_filter]

# create three columns
kpi1, kpi2, kpi3 = st.columns(3)


kpi1.metric(
    label="Gender ⏳",
    value=df_gender.groupby(['Gender']).size(),
   
)

kpi2.metric(
    label="Gender in State ⏳",
    value=df_state.groupby(['State']).size(),
   
)

kpi3.metric(
    label="Total Patient in 2016 ⏳",
    value=len(df),
   
)


# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("### Gender Chart")
    fig = px.histogram(
        data_frame=df, x= "Gender"
    )
    st.write(fig)



with fig_col2:
    st.markdown("### State  wise Gender Chart")
    fig2 = px.density_heatmap(data_frame=df, y="Gender", x="State")
    st.write(fig2)





st.markdown("### Detailed Data View")
st.dataframe(df)