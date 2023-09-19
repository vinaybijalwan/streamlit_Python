#Date:17-02-2023 time 03:46PM
import streamlit as st
import datetime as dt
import pandas as pd

# Read the CSV file
df = pd.read_csv(r'pah_2016_2022_with_Y_M_02.csv', encoding='latin1', low_memory=False)

year = (2016, 2017, 2018, 2019, 2020, 2021, 2022)

month = ('January', 'February', 'March',
         'April', 'May', 'June',
         'July', 'August', 'September', 
         'October', 'November', 'December')


df['Date'] = pd.to_datetime(df['Visit Date'])

df["YearNumber"] = df["Date"].dt.year
df["MonthNumber"] = df["Date"].dt.month


sel_year = st.sidebar.selectbox(label="selection the month", options=year)

#sel_month = st.sidebar.selectbox(label="selection the month", options=month)


year_index = year.index(sel_year)

# Get the month index based from selected month.
# We add 1 since index starts at 0 but our january starts at 1.
month_index = month.index(sel_month) + 1


dfSelection_yy = df.query(
    "YearNumber == @year.index"
)

st.dataframe(dfSelection_yy)

