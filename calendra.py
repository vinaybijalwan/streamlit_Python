import streamlit as st
import datetime

# Create a calendar widget in the sidebar
with st.sidebar:
    Start_a_date = st.date_input('Start a date')

with st.sidebar:
    End_a_date = st.date_input('End a date')
# Display the selected date in the main content area

st.write('Data from :', Start_a_date, 'to :', End_a_date) 



selected_date = st.date_input('Select a date')

# Display the selected date
st.write('Selected date:', selected_date)