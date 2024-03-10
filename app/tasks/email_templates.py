from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings


def create_email_message(
        menu: dict,
        email_to: EmailStr
):
    email = EmailMessage()

    email['Subject'] = f"Меню"
    email['From'] = settings.DB_USER
    email['To'] = email_to
    email.set_content(
        f"""
            {menu}
        
        """,
        subtype="html"
    )
    return email
