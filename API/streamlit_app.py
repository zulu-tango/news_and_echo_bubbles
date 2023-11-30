import streamlit as st
import requests

# Fonction pour appeler l'API de résumé
def call_summarization_api(text):
    #return "this is summarised text"
    response = requests.post("http://127.0.0.1:8000/summarize/", json={"text": text})
    return response.json()["summary"]

# Interface utilisateur Streamlit
st.title("Text Summarization App")

input_text = st.text_area("Enter text to summarize:")
if st.button("Summarize"):
    if input_text:
        summary = call_summarization_api(input_text)
        st.text_area("Summary:", summary)
    else:
        st.warning("Please enter some text to summarize.")
