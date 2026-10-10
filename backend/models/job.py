"""
Job Models

Defines the validated structure returned by the Job Agent.
"""

from typing import List
from pydantic import BaseModel, Field


class JobData(BaseModel):
    job_title: str = ""
    company: str = ""

    required_skills: List[str] = Field(default_factory=list)
    preferred_skills: List[str] = Field(default_factory=list)
    responsibilities: List[str] = Field(default_factory=list)
    qualifications: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)

    tone: str = ""
    summary: str = ""