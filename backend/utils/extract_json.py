import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def text_to_json(text: str):
    prompt = f"""
Extract the following resume into structured json with this format:

{{
  "personal_info": {{
    "full_name": "",
    "email": "",
    "phone": "",
    "linkedin": "",
    "github": "",
    "location": ""
  }},
  "education": [],
  "skills": [],
  "experience": [],
  "projects": [],
  "certifications": []
}}

Resume text:
{text}

Return ONLY valid JSON.
"""

    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)

    try:
        return json.loads(response.text)
    except:
        return {"error": "json_parse_failed", "raw": response.text}
