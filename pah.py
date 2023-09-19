#Create Interactive Dashboards with Streamlit and Python
#Dated: 25-01-2023


#Import Libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# st.title()- to set the title
# st.text() to write the description for the particular graph
# st.markdown() to display text as markdown
# st.latex() to display the mathematical expressions in the dashboard.
# st.write() helps to display everything such as plotly graph, dataframe, functions, model, etc.
# st.sidebar() is used for displaying data on the sidebar.
# st.dataframe() to display the data frame
# st.map() to display the map in just a single line code etc


## basic set up of Dashboad page

st.set_page_config(
    page_title="Patient Dashboard 2016-2022",
    page_icon="✅",
    layout="wide",
)




#Load the dataset

@st.experimental_memo
def load_data():
    data=pd.read_csv(r'PAH_2016_2022.csv', encoding='latin1', low_memory=False)
    return data

df = load_data()

# dashboard title
st.title("Patient Data Dashboard 2016-2022")

st.sidebar.checkbox("Show Analysis by State", True, key=1)
select = st.sidebar.selectbox('Select a State',df['State'])

#get the state selected in the selectbox
state_data = df[df['State'] == select]

select_status = st.sidebar.radio("Feedback patient's status", ('Medicine Continue',
'Medicine Discontinue', 'Patient Death', 'Other', 'NA'))




