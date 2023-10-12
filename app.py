import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from PIL import Image

image1 = Image.open('./images/salaries.jpg')
image1 = image1.resize((600,300))
image2 = Image.open('./images/salaries.jpg')


st.sidebar.image(image1)
st.sidebar.title("Select an option")
page = st.sidebar.selectbox("Explore or predict", ("Predict", "Explore")) 



if page =="Predict":
    show_predict_page()
else:
    show_explore_page()    
    

