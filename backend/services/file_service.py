"""
File Service

Handles reading uploaded files and extracting text
for AI agents to process.
"""

import os
from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text content from a PDF resume.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def save_upload(file, upload_folder="uploads") -> str:
    """
    Saves uploaded files locally and returns the file path.
    """

    Path(upload_folder).mkdir(
        exist_ok=True
    )

    file_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path