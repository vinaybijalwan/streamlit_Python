import pandas as pd
import streamlit as st
from datetime import date, timedelta


# Read the CSV file
df = pd.read_csv(r'Jan_2023.csv', encoding='latin1', low_memory=False)

# Convert the date column to a date format
df['date'] = pd.to_datetime(df['Visit Date'])


st.write(df['date'])

# Define the range of valid dates
#min_date = date.today() - timedelta(days=365)
#max_date = date.today()

min_date_01 = df['date'].min()
st.write('this is Minimum date')
st.write(min_date_01)
max_date_02 = df['date'].max()
max_date_03 = date.today()
st.write('this is Max date')
st.write(max_date_02)
st.write('this is Today date')
st.write(max_date_03)


# Create a date input widget
#selected_date = st.date_input("Select a date", min_value=min_date, max_value=max_date)

#date = st.date_input('enter a date')
# Add a date input field to the Streamlit app
#date = st.date_input('Select a date', df['date'].min(), df['date'].max())




# Filter the dataframe based on the selected date
#filtered_df = df[df['Visit Date'] == date]

# Display the filtered dataframe
#st.write(filtered_df)
