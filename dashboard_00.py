## dashboard  data analysisi with daily and weekly

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


## basic set up of Dashboad page
st.set_page_config(
    page_title="Patient Dashboard April - 2022",
    page_icon="✅",
    layout="wide",
)

##load dataset
@st.experimental_memo
def load_data():
    data=pd.read_csv(r'pah_2016_2022_with_Y_M_02.csv', encoding='latin1', low_memory=False)
    return data

df = load_data()


month = ('January', 'February', 'March',
         'April', 'May', 'June',
         'July', 'August', 'September', 
         'October', 'November', 'December')

## Year wise filter data
year_filter = st.sidebar.selectbox("Select a Year", [2016, 2017, 2018, 2019, 2020, 2021, 2022])



##load data 2016
if year_filter == 2016:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    
    

    # Create MonthNumber column based from DateTime column.
    filtered_df["MonthNumber"] = filtered_df["mm"]
    #st.dataframe(df)
    # Add streamlit selectbox.
    sel_month = st.sidebar.selectbox(label="selection the month", options=month)

    month_index = month.index(sel_month) + 1

    dfSelection = filtered_df.query(
    "MonthNumber == @month_index"
)
    st.dataframe(dfSelection)
    


