"""
API Routes
"""

from fastapi import APIRouter, UploadFile, File

from agents.resume_agent import resume_agent
from agents.job_agent import job_agent

from services.file_service import (
    save_upload,
    extract_text_from_pdf,
)

from services.email_sender import send_email

from orchestrators.outreach_orchestrator import (
    outreach_orchestrator,
)

from models.outreach_request import OutreachRequest


router = APIRouter(
    prefix="/api",
    tags=["AI Outreach Agent"],
)


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Outreach Agent",
    }


@router.post("/resume/upload")
def upload_resume(
    file: UploadFile = File(...)
):

    file_path = save_upload(file)

    resume_text = extract_text_from_pdf(
        file_path
    )

    return resume_agent.analyze_resume(
        resume_text
    )


@router.post("/job/analyze")
def analyze_job(payload: dict):

    return job_agent.analyze_job(
        payload["job_description"]
    )


@router.post("/outreach/generate")
def generate_outreach(
    request: OutreachRequest,
):

    return outreach_orchestrator.generate(
        request
    )

@router.post("/gmail/send")
def send_gmail_email(payload: dict):

    """
    Send an approved outreach email through the
    authenticated Gmail account.
    """

    return send_email(
        to=payload["to"],
        subject=payload["subject"],
        body=payload["body"],
    )