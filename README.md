# AI-Powered Resume Builder & ATS Optimization Agent

## Overview
This project builds an AI-powered resume enhancer integrated with an ATS (Applicant Tracking System) scoring mechanism. Users can upload their resumes (PDF) or manually enter resume details, receive an ATS compatibility score, enhance the resume content using Google generative AI, and download the final resume as PDF or DOCX.

---

## Features
- Upload resume in PDF format and extract text.
- Manual entry option for detailed resume creation using JSON structure.
- Compute ATS score based on job description matching.
- Enhance resume content to be ATS-friendly using Google's Gemini AI.
- Compare ATS scores before and after enhancement.
- Download enhanced resumes as PDF or DOCX files.
- Fully integrated with FastAPI backend and Streamlit frontend.
- Support for environment variable-based API key management and file storage.

---

## Tech Stack & Dependencies
- Backend: FastAPI, Uvicorn, Pydantic, Python-Multipart
- Frontend: Streamlit, Requests
- PDF/Text Processing: PyMuPDF, ReportLab, python-docx, PyPDF2
- AI & ML: google-generativeai, sentence-transformers
- Utilities: python-dotenv, Jinja2

---

## Getting Started

### Prerequisites
- Python 3.10+
- Virtualenv (recommended)

### Installation
1. Clone the repository:

2. Create and activate a virtual environment:

3. Install dependencies from requirements.txt

4. Set up environment variables (e.g., `GOOGLE_API_KEY`) in a `.env` file.


### Running Locally

**Start the backend server:**
uvicorn main:app --reload 


**Start the Streamlit frontend:**
streamlit run app.py



