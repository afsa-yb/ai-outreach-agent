"""
Outreach Response Model
"""

from pydantic import BaseModel

from models.resume import ResumeData
from models.job import JobData
from models.personalization import PersonalizationData
from models.email import EmailData


class OutreachResponse(BaseModel):

    resume: ResumeData

    job: JobData

    personalization: PersonalizationData

    email: EmailData