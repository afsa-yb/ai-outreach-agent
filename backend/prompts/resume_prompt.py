"""
Prompt used by the Resume Agent.

Keeping prompts separate from agent logic makes them easier to
maintain, test, and improve without modifying the agent code.
"""

RESUME_ANALYSIS_PROMPT = """
You are an expert AI Resume Analysis Agent.

Your task is to extract structured information from a candidate's resume.

Return ONLY valid JSON using this exact schema:

{
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
}

Rules:
- Return only JSON.
- No markdown.
- No explanations.
- Use empty string or empty list if information is missing.

Resume:

{resume}
"""