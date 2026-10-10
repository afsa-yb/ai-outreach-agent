"""
Outreach Request Model
"""

from pydantic import BaseModel

from models.resume import ResumeData


class OutreachRequest(BaseModel):

    resume: ResumeData

    job_description: str