import streamlit as st

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title("Welcome to Awesome Data Project")


with dataset:
    st.write("This is Dataset Container ")


with features:
    st.write("This is features Container")


with model_training:
    st.write("This is model_training conatiner")