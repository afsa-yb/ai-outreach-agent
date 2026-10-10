"""
Job Agent

Analyzes a job description and extracts structured hiring requirements.
"""

from services.llm_service import llm
from utils.json_parser import parse_llm_json
from models.job import JobData


class JobAgent:

    def analyze_job(self, job_description: str) -> JobData:

        prompt = f"""
You are an expert AI Job Analysis Agent.

Return ONLY valid JSON.

{{
    "job_title": "",
    "company": "",
    "required_skills": [],
    "preferred_skills": [],
    "responsibilities": [],
    "qualifications": [],
    "keywords": [],
    "tone": "",
    "summary": ""
}}

Job Description:

{job_description}
"""

        response = llm.generate_response(prompt)

        data = parse_llm_json(response)

        return JobData(**data)


job_agent = JobAgent()