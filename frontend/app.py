
import streamlit as st
import requests
import json

API = "http://localhost:8000"

st.set_page_config(page_title="AI Resume Enhancer & ATS Scorer", layout="wide")

st.title("AI Resume Enhancer & ATS Scorer")
st.write("Choose your input method, then upload or enter your resume details. Get ATS scores before and after enhancement.")

# Initialize session state keys
for key in ["resume_text", "enhanced", "initial_score", "enhanced_score"]:
    if key not in st.session_state:
        st.session_state[key] = None if "score" in key else ""

# Mode selector
input_mode = st.radio("Select Resume Input Method:", ("Upload Resume (PDF)", "Manual Entry"))

job_desc = st.text_area("Paste Job Description", height=200)

if input_mode == "Upload Resume (PDF)":
    st.subheader("Upload Resume (PDF)")
    uploaded = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded:
        with st.spinner("Extracting text…"):
            res = requests.post(
                f"{API}/upload-pdf/",
                files={"file": (uploaded.name, uploaded.getvalue(), "application/pdf")}
            )
        data = res.json()
        if "json" in data:
            st.session_state["resume_text"] = data["json"]["content"]
            st.session_state["initial_score"] = None
            st.session_state["enhanced_score"] = None
            # Calculate initial score
            st.session_state["initial_score"] = requests.post(f"{API}/score/", json={
                "resume_text": st.session_state["resume_text"],
                "job_desc": job_desc
            }).json().get("final_score")
            st.success("Text extracted successfully!")
        st.text_area("Extracted Resume", st.session_state["resume_text"], height=300)

elif input_mode == "Manual Entry":
    st.subheader("Enter Your Resume Details Manually")
    personal_info = {
        "full_name": st.text_input("Full Name"),
        "email": st.text_input("Email"),
        "phone": st.text_input("Phone"),
        "linkedin": st.text_input("LinkedIn"),
        "github": st.text_input("GitHub"),
        "location": st.text_input("Location")
    }

    education = st.text_area("Education (JSON List)", "[]")
    skills = st.text_area("Skills (JSON List)", "[]")
    experience = st.text_area("Experience (JSON List)", "[]")
    projects = st.text_area("Projects (JSON List)", "[]")
    certifications = st.text_area("Certifications (JSON List)", "[]")

    if st.button("Create Resume Text"):
        try:
            edu_list = json.loads(education)
            skills_list = json.loads(skills)
            exp_list = json.loads(experience)
            projects_list = json.loads(projects)
            certs_list = json.loads(certifications)

            resume_json_payload = {
                "personal_info": personal_info,
                "education": edu_list,
                "skills": skills_list,
                "experience": exp_list,
                "projects": projects_list,
                "certifications": certs_list
            }

            res = requests.post(f"{API}/manual-resume-text/", json=resume_json_payload)
            data = res.json()
            if "resume_text" in data:
                st.session_state["resume_text"] = data["resume_text"]
                st.session_state["initial_score"] = None
                st.session_state["enhanced_score"] = None
                st.session_state["initial_score"] = requests.post(f"{API}/score/", json={
                    "resume_text": st.session_state["resume_text"],
                    "job_desc": job_desc
                }).json().get("final_score")
                st.success("Manual resume text created! You can now score and enhance.")
                st.text_area("Resume Text", st.session_state["resume_text"], height=300)
            else:
                st.error("Failed to create resume text from input.")

        except json.JSONDecodeError:
            st.error("Please enter valid JSON lists for each section.")

# Compute initial score button
if st.button("Compute Initial Score"):
    if st.session_state["resume_text"]:
        res = requests.post(f"{API}/score/", json={"resume_text": st.session_state["resume_text"], "job_desc": job_desc})
        st.session_state["initial_score"] = res.json().get("final_score")
        st.success(f"Initial ATS Score: {st.session_state['initial_score']}")
    else:
        st.warning("Please provide resume text first.")

# Enhance resume button
if st.button("Enhance Resume"):
    if st.session_state["resume_text"]:
        with st.spinner("Enhancing resume... Please wait."):
            res = requests.post(
                f"{API}/enhance/",
                json={"resume_text": st.session_state["resume_text"], "job_desc": job_desc}
            )
        raw = res.json()
        if "error" in raw:
            st.error(f"Backend Error: {raw['error']}")
        else:
            st.session_state["enhanced"] = raw["enhanced_text"]
            score_res = requests.post(f"{API}/score/", json={"resume_text": raw["enhanced_text"], "job_desc": job_desc})
            st.session_state["enhanced_score"] = score_res.json().get("final_score")
            st.text_area("Enhanced Resume", raw["enhanced_text"], height=300)
    else:
        st.warning("Please provide resume text first.")

# Show ATS Score comparison if both scores available
if st.session_state["initial_score"] is not None and st.session_state["enhanced_score"] is not None:
    st.subheader("ATS Score Comparison")
    st.markdown(f"**Before Enhancement:** {st.session_state['initial_score']}  |  **After Enhancement:** {st.session_state['enhanced_score']}")

# Download buttons
st.subheader("Download Enhanced Resume")
if st.button("Generate PDF"):
    if st.session_state["enhanced"]:
        res = requests.post(f"{API}/download-pdf/", json={"resume_text": st.session_state["enhanced"]})
        raw = res.json()
        file_id = raw["file_id"]
        st.success("PDF Generated!")
        st.markdown(f"[**Download PDF**](http://localhost:8000/storage/{file_id}.pdf)")
    else:
        st.warning("Please enhance resume first.")

if st.button("Generate DOCX"):
    if st.session_state["enhanced"]:
        res = requests.post(f"{API}/download-docx/", json={"resume_text": st.session_state["enhanced"]})
        raw = res.json()
        file_id = raw["file_id"]
        st.success("DOCX Generated!")
        st.markdown(f"[**Download DOCX**](http://localhost:8000/storage/{file_id}.docx)")
    else:
        st.warning("Please enhance resume first.")
