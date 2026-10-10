"""
Personalization Model

Represents the AI strategy used to personalize
the outreach email.
"""

from pydantic import BaseModel


class PersonalizationData(BaseModel):

    highlighted_skills: list[str]

    best_project: str

    keywords: list[str]

    company_tone: str

    email_strategy: str

    reasoning: str