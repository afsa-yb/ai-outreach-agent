"""
JSON Parser
-----------

LLMs don't always return perfect JSON. Sometimes they wrap the response
inside Markdown code blocks or add extra text.

This utility extracts the JSON safely so every agent can reuse the same logic.
"""

import json
import re
from typing import Any


def parse_llm_json(response: str) -> Any:
    """
    Convert an LLM response into a Python object.

    Raises:
        ValueError: If valid JSON cannot be extracted.
    """

    if not response:
        raise ValueError("LLM returned an empty response.")

    # Remove Markdown code fences if present.
    cleaned = re.sub(r"```json|```", "", response).strip()

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError:
        pass

    # Try extracting the first JSON object from the response.
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)

    if not match:
        raise ValueError("No valid JSON object found in the LLM response.")

    try:
        return json.loads(match.group())
    except json.JSONDecodeError as error:
        raise ValueError("Unable to parse JSON returned by the LLM.") from error