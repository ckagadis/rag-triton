import streamlit as st
import requests

st.title("ragmaster")

query = st.text_input("Ask a question:")

if query:
    resp = requests.post("http://rag-backend:8000/query", json={"question": query})
    st.write(resp.json())
