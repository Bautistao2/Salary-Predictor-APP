import streamlit as st
import pickle
import numpy as np
import pickle

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
         data = pickle.load(file)
    return data

data = load_model()


lre = data["model"]
lenc_country = data["lenc_country"] 
level_education = data["level_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    
    st.write("""### We need some information to predict the salary""")

 
    countries = (
        "United States of America",                             
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada ",
        "India",
        "France ",
        "Netherlands",
        "Australia",
        "Brazil",
        "Spain",
        "Sweden",
        "Italy ",
        "Poland ",
        "Switzerland",
        "Denmark",
        "Norway",
        "Israel",
    )
    
    education = (
        "Bachelor’s degree",
        "College",
        "Master’s degree",
        "Professional degree",
        "Associate degree", 
        "Secondary school",
        "Elementary school",
        "Other",
    )
    
    country = st.selectbox("Select the country", countries)
    education = st.selectbox("Select the education level", education) 
    
    experience = st.slider("Years of Experience")
     
    yes= st.button("Calculate Salary")
    if yes:
        x = np.array([[country, education, experience]])
        x[:, 0] = lenc_country.transform(x[:,0])
        x[:, 1] =level_education.transform(x[:,1])
        x = x.astype(float)
        
        salary = lre.predict(x)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
        
        
        
    
        
        
