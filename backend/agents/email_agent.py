"""
Email Agent

Generates personalized outreach emails.
"""

import json

from services.llm_service import llm
from utils.json_parser import parse_llm_json

from models.email import EmailData
from prompts.email_prompt import EMAIL_GENERATION_PROMPT


class EmailAgent:

    def generate_email(
        self,
        resume: dict,
        job: dict,
        personalization: dict,
    ) -> EmailData:

        prompt = EMAIL_GENERATION_PROMPT.format(
            resume=json.dumps(
                resume,
                indent=2
            ),
            job=json.dumps(
                job,
                indent=2
            ),
            personalization=json.dumps(
                personalization,
                indent=2
            ),
        )

        response = llm.generate_response(
            prompt
        )

        data = parse_llm_json(
            response
        )

        return EmailData(
            **data
        )


email_agent = EmailAgent()