"""
Outreach Orchestrator

Coordinates the complete AI outreach workflow.
"""

from agents.job_agent import job_agent
from agents.personalization_agent import personalization_agent
from agents.email_agent import email_agent

from models.outreach_request import OutreachRequest
from models.outreach_response import OutreachResponse


class OutreachOrchestrator:

    def generate(
        self,
        request: OutreachRequest,
    ) -> OutreachResponse:

        # Step 1
        job = job_agent.analyze_job(
            request.job_description
        )

        # Step 2
        personalization = personalization_agent.analyze(
            resume=request.resume.model_dump(),
            job=job.model_dump(),
        )

        # Step 3
        email = email_agent.generate_email(
            resume=request.resume.model_dump(),
            job=job.model_dump(),
            personalization=personalization.model_dump(),
        )

        # Step 4
        return OutreachResponse(
            resume=request.resume,
            job=job,
            personalization=personalization,
            email=email,
        )


outreach_orchestrator = OutreachOrchestrator()