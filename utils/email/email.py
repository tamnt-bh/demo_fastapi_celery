from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From
from sendgrid.helpers.mail import Mail

from common.config import settings
from static.email import email_template
from utils.email.entity import TemplateContent, Template


class Email:
    def __init__(self, to_email: str, fullname: str):
        self._from_email = From(settings.EMAIL_FROM, settings.NAME_EMAIL_FROM)
        self._to = to_email
        self._fullname = fullname

    def _send(self, html_content: str, plain_text_content: str, subject):
        message = Mail(
            from_email=From(settings.EMAIL_FROM, settings.NAME_EMAIL_FROM),
            to_emails=self._to,
            subject=subject,
            html_content=html_content,
            plain_text_content=plain_text_content,
        )

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        sg.send(message)

    def send_register_success(self):
        template = email_template[Template.REGISTER_SUCCESS]
        html_content = template[TemplateContent.HTML].replace(
            "{{NAME}}", self._fullname
        )
        plain_text_content = template[TemplateContent.PLAIN_TEXT].replace(
            "{{NAME}}", self._fullname
        )

        self._send(html_content, plain_text_content, "Welcome")

    def send_reminder_buying(self):
        template = email_template[Template.REMINDER_BUYING]
        html_content = template[TemplateContent.HTML].replace(
            "{{NAME}}", self._fullname
        )
        plain_text_content = template[TemplateContent.PLAIN_TEXT].replace(
            "{{NAME}}", self._fullname
        )

        self._send(html_content, plain_text_content, "Reminder")
