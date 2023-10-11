import streamlit as st
from predict_page import show_predict_page


st.sidebar.st.selectbox("Explore or predict", ("Predict", "Explore")) 

show_predict_page()
