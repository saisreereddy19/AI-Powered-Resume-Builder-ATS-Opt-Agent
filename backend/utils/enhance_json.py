import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def enhance_resume_json(resume_text, job_desc):
    prompt = f"""
    Return only the enhanced resume text. Do NOT include explanations, summaries, or improvement notes.
You are an ATS resume expert.
Rewrite & improve the resume for this job description:
{job_desc}

Enhance wording, add ATS keywords, fix grammar,
BUT KEEP THE SAME JSON STRUCTURE.

Resume content:
{resume_text}

Return:
1. Enhanced JSON (first)
2. Enhanced plain text version (after '---TEXT---')
"""

    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)

    cleaned = response.text.split("---TEXT---")

    json_part = json.loads(cleaned[0])
    text_part = cleaned[1].strip()

    return json_part, text_part
