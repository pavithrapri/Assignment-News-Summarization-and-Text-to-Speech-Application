import requests
import streamlit as st

API_URL = "http://127.0.0.1:5000/analyze"

st.title("News Summarization & Sentiment Analysis")

company = st.text_input("Enter Company Name")

if st.button("Analyze"):
    response = requests.post(API_URL, json={"company": company})
    
    if response.status_code == 200:
        data = response.json()
        
        st.write("### Sentiment Analysis Report")
        st.json(data)
        
        if "Audio" in data:
            st.audio("output.mp3")
    else:
        st.error("Failed to fetch data. Try again!")
