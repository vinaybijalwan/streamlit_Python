import pandas as pd

import streamlit as st
import chart_studio.plotly as plt
#import plotly.plotly as plt
import plotly.express as px 


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


st.title("Hospital Data Visualization")

if st.checkbox("Show Data"):
    st.write(df)



year_filter = st.selectbox("Select a Year", [2016, 2017, 2018, 2019, 2020, 2021, 2022])
filtered_df = df[df['yyyy'] == year_filter]

st.write("Data for year: ", year_filter)

st.write('Total patient    ', year_filter, ' in Patanjali Ayurveda  Hospital ', len(filtered_df))
if st.checkbox("Show Data Year Wise"):
    st.write(filtered_df.head(100))


total_patients = st.number_input("Total Patients", value=0, min_value=0, max_value=None, step=1)

st.write("Total Patients: ", total_patients)



#if st.checkbox("Show Graph by Year"):
#    chart_data = df.groupby("yyyy").count()
#    st.bar_chart(chart_data)

if st.checkbox("Show Graph by Year"):
    chart_data = df.groupby("yyyy").count()
    st.altair_chart(chart_data)


if st.checkbox("Show Graph by Gender"):
    chart_data = df.groupby("Gender").count()
    st.bar_chart(chart_data)



if st.checkbox("Show Graph by State"):
    chart_data = df.groupby("State").count()
    st.bar_chart(chart_data)

if st.checkbox("Show Graph by Doctor vs Disease"):
    chart_data = df.groupby(["Vaidya Name", "Disease"]).count()
    st.bar_chart(chart_data)
