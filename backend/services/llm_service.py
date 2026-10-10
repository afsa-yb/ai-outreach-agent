"""
LLM Service
-----------

This module is the single entry point for every Large Language Model request.

Why keep everything here?

Instead of allowing every agent to directly communicate with the AI model,
all agents call this service.

Benefits:
- Easy to swap providers (Groq, OpenAI, Gemini, Ollama...)
- Centralized error handling
- Cleaner architecture
- Easier testing and maintenance
"""

import os

from groq import Groq
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


class LLMService:
    """
    Handles all communication with the language model.
    """

    def __init__(self) -> None:

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found inside .env"
            )

        self.client = Groq(api_key=api_key)

        # Fast, powerful and currently free.
        self.model = "openai/gpt-oss-120b"

    def generate_response(
        self,
        prompt: str,
        system_prompt: str = "You are a helpful AI assistant."
    ) -> str:
        """
        Sends a prompt to the LLM and returns plain text.
        """

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                temperature=0.3,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            return response.choices[0].message.content.strip()

        except Exception as error:
            raise RuntimeError(
                f"LLM request failed: {error}"
            ) from error


# Shared instance used throughout the project.
llm = LLMService()
