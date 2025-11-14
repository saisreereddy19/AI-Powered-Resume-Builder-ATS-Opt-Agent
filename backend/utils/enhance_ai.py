import google.generativeai as genai
import os

import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

PROMPT = """
You are a world-class resume writer. Improve the following resume text for ATS, clarity, impact, and professional tone.
Also integrate relevant keywords from the job description if they fit naturally.

Resume:
{resume}

Job Description:
{jd}

Return improved resume text only. Keep formatting clean.
"""

def improve_resume(resume, jd):
    text = PROMPT.format(resume=resume, jd=jd)
    res = model.generate_content(text)
    return res.text
