"""
Personalization Agent

Analyzes the resume and job description to determine
the best way to personalize the outreach email.
"""

import json

from services.llm_service import llm
from utils.json_parser import parse_llm_json

from prompts.personalization_prompt import PERSONALIZATION_PROMPT
from models.personalization import PersonalizationData


class PersonalizationAgent:

    def analyze(
        self,
        resume: dict,
        job: dict,
    ) -> PersonalizationData:

        prompt = PERSONALIZATION_PROMPT.format(
            resume=json.dumps(resume, indent=2),
            job=json.dumps(job, indent=2),
        )

        response = llm.generate_response(prompt)

        data = parse_llm_json(response)

        return PersonalizationData(
            **data
        )


personalization_agent = PersonalizationAgent()