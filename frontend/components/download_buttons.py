import streamlit as st
import requests
import json

def download_buttons(API, data):
    j = json.dumps(data)

    pdf = requests.post(f"{API}/generate/pdf/", data={"data": j})
    st.download_button("Download PDF", pdf.content, file_name="Enhanced_Resume.pdf")

    docx = requests.post(f"{API}/generate/docx/", data={"data": j})
    st.download_button("Download DOCX", docx.content, file_name="Enhanced_Resume.docx")
