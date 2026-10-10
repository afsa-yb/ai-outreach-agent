"""
Prompt used by the Job Agent.
"""

JOB_ANALYSIS_PROMPT = """
You are an expert AI Job Analysis Agent.

Analyze the following job description and return ONLY valid JSON.

Schema:

{
    "job_title": "",
    "company": "",
    "required_skills": [],
    "preferred_skills": [],
    "responsibilities": [],
    "qualifications": [],
    "keywords": [],
    "tone": "",
    "summary": ""
}

Rules:
- Return only JSON.
- No markdown.
- No explanations.
- Use empty strings or empty lists where information is unavailable.

Job Description:

{job_description}
"""