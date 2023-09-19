##this file first design layout of Dashboard
#date 17-02-2023

import streamlit as st
import pandas as pd


## basic set up of Dashboad page
st.set_page_config(
    page_title="Patient Dashboard 2016 - 2022",
    page_icon="✅",
    layout="wide",
)

##load dataset
@st.experimental_memo
def load_data():
    data=pd.read_csv(r'pah_2016_2022_with_Y_M_02.csv', encoding='latin1', low_memory=False)
    return data

df = load_data()


# Create a calendar widget in the sidebar
with st.sidebar:
    Start_a_date = st.date_input('Start a date')
    End_a_date = st.date_input('End a date')

    st.write('Data from :', Start_a_date, 'to :', End_a_date) 


container1 = st.container()


with st.container():
   col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(label="Total Patient", value=len(df), delta="1.2 ")

with col2:
    st.metric("Active Diease Category", df['Category'].nunique(), "-8%")

with col3:
    st.metric("Active Disease", df['Disease'].nunique(), "4%")


with col4:
    st.metric(label="Active Doctor's", value=df['Vaidya Name'].nunique(), delta=123,
    delta_color="off")


col1, col2 = st.columns(2)

col1.metric(label="Average Patient", value=2345, delta="+20%")

col2.metric(label="Gender", value=456, delta="+20%")