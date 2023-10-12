import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i]>= cutoff:
            categorical_map[categories.index[i]]= categories.index[i]
        else:
                categorical_map[categories.index[i]]='Other'
    return categorical_map

def clean_years(x):
    if x == 'Less than 1 year':
        return 0.5
    if x == 'More than 50 years':
        return 50
    return float(x)


def clean_education(x):
    if x == 'Bachelor’s degree (B.A., B.S., B.Eng., etc.)':
        return "Bachelor’s degree"
    if x == 'Some college/university study without earning a degree':
        return "College"
    if x == 'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)':
        return "Master’s degree"
    if x == 'Professional degree (JD, MD, Ph.D, Ed.D, etc.)':
        return "Professional degree"
    if x == 'Associate degree (A.A., A.S., etc.)':
        return "Associate degree"
    if x == 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)':
        return "Secondary school"
    if x ==  'Primary/elementary school':
        return "Elementary school"
    if x == 'Something else':
        return "Other"


@st.cache_resource
def load_data():
    df=pd.read_csv("./env/surveydata.csv")
    df = df[["Country","EdLevel","YearsCode", "Employment","ConvertedCompYearly"]]
    df = df[df["ConvertedCompYearly"].notnull()]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df.dropna()
    df =  df [df["Employment"] == "Employed, full-time"]
    
    country_map = shorten_categories(df.Country.value_counts(),400)
    df['Country']= df['Country'].map(country_map)
    df=df[df["Salary"]<=250000]
    df= df[df["Salary"]>= 20000]
    df= df[df['Country']!= "Other"]
    
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    df['YearsCode'] = df['YearsCode'].apply(clean_years)
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    return df

df = load_data()


def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    
    st.write("Stack Overflow Developer Survey 2023")
  
   
    
    data = df ["Country"].value_counts()
    
    fig1,ax1 = plt.subplots(figsize=(20,20,))
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90, textprops={'fontsize': 25})
    ax1.axis("equal")
    
    
    st.write(""" ### Number of Data From different countries""")
    
    st.pyplot(fig1)
   
    
    st.write(""" ### Main Salary Based On Country""")
    
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    
    st.write(""" ### Main Salary Based On Country""")
    data = df.groupby(["YearsCode"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
    
    

    
    
