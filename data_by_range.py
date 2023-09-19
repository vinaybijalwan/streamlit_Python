import streamlit as st
import pandas as pd
import datetime

# Load the data from a CSV file
data = pd.read_csv('PAH_April_2022.csv', parse_dates=['Visit Date'])

# Create a calendar widget to select the date range
start_date = st.date_input('Start date')
end_date = st.date_input('End date')

# Filter the data based on the selected date range
filtered_data = data[(data['Visit Date'] >= start_date) & (data['Visit Date'] <= end_date)]

# Display the count of data by date
data_by_date = filtered_data.groupby('Visit Date').size().reset_index(name='count')
st.line_chart(data_by_date.set_index('Visit Date'))
