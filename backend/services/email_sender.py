"""
Email Sender

Sends an email through the authenticated Gmail account.
"""

import base64
from email.mime.text import MIMEText

from services.gmail_service import get_gmail_service


def send_email(
    to: str,
    subject: str,
    body: str,
):
    service = get_gmail_service()

    message = MIMEText(body)

    message["to"] = to
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    result = service.users().messages().send(
        userId="me",
        body={
            "raw": raw_message
        }
    ).execute()

    return result