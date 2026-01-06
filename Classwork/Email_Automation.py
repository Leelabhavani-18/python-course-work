import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "leelabhavani1805@gmail.com"
SENDER_PASSWORD = "tuqj zazv ijso sdiu"

def send_mail(to_email, subject, body, attachments=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        
        msg.attach(MIMEText(body, "plain"))

        
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        mime_base = MIMEBase("application", "octet-stream")
                        mime_base.set_payload(f.read())
                        encoders.encode_base64(mime_base)
                        mime_base.add_header(
                            "Content-Disposition",
                            f"attachment; filename={os.path.basename(file_path)}"
                        )
                        msg.attach(mime_base)
                else:
                    print(f"File '{file_path}' not found. Skipping.")

        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")



send_mail(
    to_email="leelabhavani1805@gmail.com",
    subject="Test Mail",
    body="Hello, this is a test email from Python"
)

