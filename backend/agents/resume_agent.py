"""
Resume Agent

Analyzes resume text and returns validated structured data.
"""

from services.llm_service import llm
from models.resume import ResumeData
from utils.json_parser import parse_llm_json


class ResumeAgent:

    def analyze_resume(self, resume_text: str) -> ResumeData:

        prompt = f"""
You are an expert resume analysis AI.

Extract information from the resume below.

Return ONLY valid JSON matching this schema.

{{
    "name": "",
    "email": "",
    "phone": "",
    "education": [],
    "skills": [],
    "projects": [],
    "experience": [],
    "certifications": [],
    "achievements": [],
    "summary": ""
}}

Rules:
- Return only JSON.
- Do not use markdown.
- Do not explain anything.

Resume:

{resume_text}
"""

        response = llm.generate_response(prompt)

        data = parse_llm_json(response)

        return ResumeData(**data)


resume_agent = ResumeAgent()