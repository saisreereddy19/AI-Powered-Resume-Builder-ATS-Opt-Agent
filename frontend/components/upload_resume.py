import streamlit as st
import requests

def upload_section(API):
    file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
    if file:
        res = requests.post(f"{API}/parse/", files={"file": file}).json()
        return res["text"]
    return ""
