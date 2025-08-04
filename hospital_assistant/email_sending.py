import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from langchain_community.llms import Ollama 

load_dotenv()

llm = Ollama(model="llama3")  

def generate_email_content(doctor_name, time, patient_name):
    prompt = f"""
Generate only the email body (no preface or explanation). Confirm an appointment with the following details:

- Patient Name: {patient_name}
- Doctor Name: Dr. {doctor_name}
- Appointment Time: {time}

Include:
- A greeting addressing the patient by name
- Confirmation of appointment details
- A reminder to arrive early and bring medical reports
- A warm closing and team signature

Do not include placeholder names or a subject line — only the email content.
"""

    return llm.invoke(prompt).strip()

def send_email(to_email, doctor_name, time, patient_name="Patient"):
    message_body = generate_email_content(doctor_name, time, patient_name)

    msg = MIMEText(message_body)
    msg["Subject"] = "✅ Appointment Confirmation"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email

    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        server.send_message(msg)
