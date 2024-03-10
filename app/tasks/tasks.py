from pydantic import EmailStr

from app.config import settings
from app.tasks.config import celery_app
from app.tasks.email_templates import create_email_message

import smtplib


@celery_app.task
def send_email(menu: dict, email_to: EmailStr):
    msg = create_email_message(menu, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)
